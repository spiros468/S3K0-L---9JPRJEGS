from __future__ import annotations
import tkinter as tk
from tkinter import ttk


class BillDetailScreen:
    def __init__(self, root, amount, date, treatement, bill_id, is_paid=False, pay_command=None, back_command=None):
        self.root = root
        self.back_command = back_command
        self.amount = amount
        self.date = date
        self.treatment = treatement
        self.bill_id = bill_id
        self.is_paid = is_paid
        self.pay_command = pay_command
        self.root.title("Bill Details")
        self.root.geometry("400x600")
        self.root.configure(bg="#ffffff")


        # --- Top Header (Title & Amount) ---
        header_frame = tk.Frame(root, bg="#ffffff")
        header_frame.pack(fill="x", pady=20)

        tk.Label(header_frame, text="BILL PAYMENT",
                 font=("Arial", 10, "bold"), bg="#ffffff", fg="#666").pack()

        # Large Amount Label matching image_8f56f9.png
        tk.Label(header_frame, text=self.amount,
                 font=("Arial", 36, "bold"), bg="#ffffff", fg="#1a1c3d").pack(pady=10)

        # --- Details Section (The "Card") ---
        # We use a frame with a slight border to group information
        details_card = tk.Frame(root, bg="#f9f9f9", bd=1, relief="solid")
        details_card.pack(padx=30, fill="x", pady=10)

        # Internal Padding for the card
        inner = tk.Frame(details_card, bg="#f9f9f9")
        inner.pack(padx=15, pady=15, fill="x")

        # Rows of information
        self.add_info_row(inner, "Issue Date", self.date, "📅")
        self.add_divider(inner)
        self.add_info_row(inner, "Description", self.treatment, "✎")
        self.add_divider(inner)
        self.add_info_row(inner, "Bill ID", self.bill_id, None)

        # --- Reminder Section ---
        reminder_frame = tk.Frame(root, bg="#f9f9f9", bd=1, relief="solid")
        reminder_frame.pack(padx=30, fill="x", pady=10)

        #tk.Label(reminder_frame, text="🔔 3 days before due date",
                 #font=("Arial", 10), bg="#f9f9f9", padx=15, pady=12).pack(side="left")

        # --- Bottom Action Buttons ---
        btn_frame = tk.Frame(root, bg="#ffffff")
        btn_frame.pack(side="bottom", fill="x", pady=30, padx=30)

        # New Back Button
        tk.Button(btn_frame, text="← Back", font=("Arial", 10),
                  bg="#ffffff", fg="#666", relief="flat",
                  command=self.back_command).pack(side="left")

        # Outline Style Button
        #tk.Button(btn_frame, text="Schedule", font=("Arial", 10, "bold"),
         #         bg="#ffffff", fg="#007bff", bd=1, relief="solid",
          #        width=12, height=2).pack(side="left")
        # Conditional Logic for Pay Button vs. Paid Message
        if is_paid:
            # Display a friendly "Already Paid" message instead of a button
            tk.Label(btn_frame, text="✓ Bill already Paid", font=("Arial", 10, "bold"),
                     bg="#ffffff", fg="#28a745").pack(side="right", pady=10)
        else:
            # Show the blue Pay button only if unpaid
            # Inside BillDetailScreen __init__
            tk.Button(btn_frame, text="Pay", font=("Arial", 10, "bold"),
                      bg="#007bff", fg="white", relief="flat",
                      width=12, height=2,
                      command=self.pay_command).pack(side="right")

            '''
            tk.Button(btn_frame, text="Pay", font=("Arial", 10, "bold"),
                      bg="#007bff", fg="white", relief="flat",
                      width=12, height=2).pack(side="right")
            '''
        # Solid Style Button
        #tk.Button(btn_frame, text="Pay", font=("Arial", 10, "bold"),
         #         bg="#007bff", fg="white", relief="flat",
          #        width=12, height=2).pack(side="right")

    def add_info_row(self, parent, label, value, icon):
        """Helper to create the small label above the bold value."""
        row_frame = tk.Frame(parent, bg="#f9f9f9")
        row_frame.pack(fill="x", pady=5)

        tk.Label(row_frame, text=label, font=("Arial", 8), fg="#888", bg="#f9f9f9").pack(anchor="w")

        val_line = tk.Frame(row_frame, bg="#f9f9f9")
        val_line.pack(fill="x")

        if icon:
            tk.Label(val_line, text=icon, font=("Arial", 10), bg="#f9f9f9").pack(side="left")

        tk.Label(val_line, text=value, font=("Arial", 11, "bold"), bg="#f9f9f9").pack(side="left", padx=5)

    def add_divider(self, parent):
        """Helper to add a subtle line between rows."""
        tk.Frame(parent, height=1, bg="#eee").pack(fill="x", pady=8)

''''
if __name__ == "__main__":
    app_root = tk.Tk()
    app = BillDetailScreen(app_root, "5000$", "2023-08-09", "Chemotherapy, Basic screening", "B003")
    app_root.mainloop()
'''