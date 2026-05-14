from Bill_Payment.Screens.payment_methods_screen import PaymentMethodScreen
from Bill_Payment.Screens.payment_form_screen import PaymentFormScreen
from Bill_Payment.Screens.receipt_screen import ReceiptScreen
from tkinter import messagebox
import pandas as pd
import os
from pathlib import Path


class PaymentManager:
    def __init__(self, root, bill_manager):
        self.root = root
        self.bill_manager = bill_manager  # Reference to go back to bills
        self.current_bill_id = None

    def display_payment_methods(self, bill_id, amount):
        """Clears screen and shows the selection (Debit/Credit)."""
        self.current_bill_id = bill_id

        # Clear the current UI
        for widget in self.root.winfo_children():
            widget.destroy()

        # Initialize the screen
        # Pass callbacks for what happens when a user clicks a method
        return PaymentMethodScreen(
            self.root,
            amount,
            back_command=lambda: self.bill_manager.handle_bill_selection(bill_id),
            on_debit=lambda: self.display_payment_form("Debit", amount, bill_id),
            on_credit=lambda: self.display_payment_form("Credit", amount, bill_id),
        )

    def get_payment_form(self):
        pass

    def display_payment_form(self, method_type, amount, bill_id):
        """Shows the actual card input fields."""
        for widget in self.root.winfo_children():
            widget.destroy()

        return PaymentFormScreen(
            self.root,
            method_type,
            amount,
            bill_id,
            on_success=lambda: self.process_final_payment(bill_id, amount, method_type),
            back_command=lambda: self.display_payment_methods(bill_id, amount)
        )

    def process_final_payment(self, bill_id, amount, method):
        """
        Triggered when the card details are validated.
        """
        # Attempt to update the CSV
        success = self.update_bill_status(bill_id)

        if success:
            # Get current date for the receipt
            from datetime import datetime
            today = datetime.now().strftime("%Y-%m-%d")

            # Clear screen and show Receipt
            for widget in self.root.winfo_children():
                widget.destroy()

            return ReceiptScreen(
                self.root,
                bill_id,
                amount,
                method,  # Pass "Debit Card" or "Credit Card"
                today,
                close_command=self.bill_manager.display_bills
            )

    def validate_payment(self):
        pass

    def update_bill_status(self, bill_id):

        try:
            # 1. Define the path to your CSV
            parent_dir = Path.cwd().parent.parent
            csv_path = os.path.join(parent_dir, "archive (1)", "final_billing.csv")

            # 2. Load the current data
            df = pd.read_csv(csv_path)

            # 3. Update the status
            # We find the row where bill_id matches and change the 'payment_status' column
            if bill_id in df['bill_id'].values:
                df.loc[df['bill_id'] == bill_id, 'payment_status'] = "Paid"

                # 4. Save the file back to disk
                df.to_csv(csv_path, index=False)
                print(f"Successfully updated Bill {bill_id} to 'Paid'.")
                return True
            else:
                print(f"Error: Bill ID {bill_id} not found in CSV.")
                return False

        except Exception as e:
            print(f"An error occurred while updating the CSV: {e}")
            return False


