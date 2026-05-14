from pathlib import Path
import numpy as np
import pandas as pd
import os.path
import tkinter as tk
from Bill_Payment.Screens.bill_management_screen import BillingDashboard
from Bill_Payment.Screens.bill_management_screen import apply_style
from Bill_Payment.Screens.bill_details_screen import BillDetailScreen
from Bill_Payment.File_Handlers.readerHandlers import BillingReader
from payment_manager import PaymentManager


class BillManager:
    def __init__(self, patient, root):
        self.patient = patient
        self.patient_bills = None
        self.root = root
        self.current_screen = None
        self.payment_mgr = PaymentManager(self.root, self)  # Pass self so it can go back

    def get_patient_bills(self):
        #get patient bills data from Reader Class
        parent_dir = Path.cwd().parent.parent
        billing_data = pd.read_csv(os.path.join(parent_dir, "archive (1)", "final_billing.csv"))
        #billing_data = BillingReader(os.path.join(parent_dir, "archive (1)", "final_billing.csv"))

        #filtering the data
        billing_data.query(f'patient_id == "{self.patient}"', inplace=True)

        data = pd.DataFrame()
        data["Date"] = billing_data["bill_date"]
        #data["Date"] = billing_data.getBillDate()
        data["Bill_id"] = billing_data["bill_id"]
        #data["Bill_id"] = billing_data.getBillId()
        data["Status"] = billing_data["payment_status"]
        #data["Status"] = billing_data.getBillPaymentStatus()
        data["Amount"] = billing_data["amount"]
        #data["Amount"] = billing_data.getBillAmount()

        self.patient_bills = data

    def display_bills(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.get_patient_bills()

        pending_bills = []
        non_pending_bills = []
        data = np.array(self.patient_bills)

        for bill in data:
            if bill[2] == "Pending":
                pending_bills.append(bill)
            else:
                non_pending_bills.append(bill)

        if not pending_bills:
            self.current_screen = BillingDashboard(
                self.root,
                np.array(non_pending_bills),
                on_select=self.handle_bill_selection
            )
            return
            #return BillingDashboard(self.root, np.array(non_pending_bills))
        elif not non_pending_bills:
            self.current_screen = BillingDashboard(
                self.root,
                np.array(pending_bills),
                on_select=self.handle_bill_selection
            )
            return
            #return BillingDashboard(self.root, np.array(pending_bills))
        self.current_screen = BillingDashboard(
            self.root,
            np.concatenate((np.array(pending_bills), np.array(non_pending_bills)), axis=0),
            on_select=self.handle_bill_selection
        )
        #return BillingDashboard(self.root, np.concatenate((np.array(pending_bills), np.array(non_pending_bills)), axis=0))

    def handle_bill_selection(self, bill_id):
        """ This is the 'Switching Logic' hub """
        # 1. Clear the current dashboard widgets
        for widget in self.root.winfo_children():
            widget.destroy()


        parent_dir = Path.cwd().parent.parent
        billing_data = pd.read_csv(os.path.join(parent_dir, "archive (1)", "final_billing.csv"))
        t_id = billing_data.query(f'bill_id == "{bill_id}"')["treatment_id"].item()

        # 3. Switch to the details screen
        self.display_bill_details(t_id)

    def display_bill_details(self, treatment_id):
        parent_dir = Path.cwd().parent.parent
        treatments = pd.read_csv(os.path.join(parent_dir, "archive (1)", "final_treatments.csv"))
        billing_data = pd.read_csv(os.path.join(parent_dir, "archive (1)", "final_billing.csv"))

        amount = billing_data.query(f'treatment_id == "{treatment_id}"')["amount"].item()
        date = billing_data.query(f'treatment_id == "{treatment_id}"')["bill_date"].item()
        bill_id = billing_data.query(f'treatment_id == "{treatment_id}"')["bill_id"].item()

        # filtering the data
        treatments.query(f'treatment_id == "{treatment_id}"', inplace=True)
        treatment_type = treatments["treatment_type"].item()
        description = treatments["description"].item()

        status = billing_data.query(f'treatment_id == "{treatment_id}"')["payment_status"].item()
        is_paid = (status.lower() == "paid")

        return BillDetailScreen(
            self.root,
            amount,
            date,
            f"{treatment_type}: {description}",
            bill_id,
            is_paid=is_paid,
            pay_command=lambda: self.payment_mgr.display_payment_methods(bill_id, amount),  # NEW
            back_command=self.display_bills
        )

        #return BillDetailScreen(self.root, amount, date, f"{treatment_type}: {description}", bill_id, is_paid, back_command=self.display_bills)


    def check_bill_status(self, bill):
        if bill[2] == "Pending":
            return 0
        else:
            return 1

'''
if __name__ == "__main__":

    app_root = tk.Tk()
    bill = BillManager("P001", app_root)
    bill.get_patient_bills()
    billing_screen = bill.display_bills()
    #details_screen = bill.display_bill_details("T004")
    apply_style()
    app_root.mainloop()

'''
if __name__ == "__main__":
    app_root = tk.Tk()
    app_root.title("Healthcare Billing System")
    app_root.geometry("900x600")

    # 1. Apply the style once at the start
    apply_style()

    # 2. Initialize the Manager
    # Use a valid patient ID from your CSV (e.g., "P001")
    manager = BillManager("P036", app_root)

    # 3. Display the initial dashboard
    # This will now call get_patient_bills() and setup the Treeview
    manager.display_bills()

    app_root.mainloop()
