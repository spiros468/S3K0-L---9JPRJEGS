import tkinter as tk


class ReceiptScreen:
    def __init__(self, root, bill_id, amount, method, date, close_command):
        self.root = root
        self.root.configure(bg="#f8f9fa")

        # --- Success Icon & Title ---
        tk.Label(self.root, text="✓", font=("Arial", 48), bg="#f8f9fa", fg="#28a745").pack(pady=(50, 10))
        tk.Label(self.root, text="Payment Successful", font=("Arial", 16, "bold"),
                 bg="#f8f9fa", fg="#1a1c3d").pack()

        # --- Receipt Card ---
        receipt_card = tk.Frame(self.root, bg="#ffffff", bd=1, relief="solid", padx=20, pady=20)
        receipt_card.pack(pady=30, padx=40, fill="x")

        self.add_receipt_row(receipt_card, "Transaction ID", f"TXN-{bill_id}")
        self.add_receipt_row(receipt_card, "Date", date)
        self.add_receipt_row(receipt_card, "Payment Method", method)

        # Divider
        tk.Frame(receipt_card, height=1, bg="#eeeeee").pack(fill="x", pady=15)

        # Total Amount
        self.add_receipt_row(receipt_card, "Total Paid", amount, is_total=True)

        # --- Back to Home Button ---
        tk.Button(self.root, text="Back to Dashboard", font=("Arial", 11, "bold"),
                  bg="#007bff", fg="white", relief="flat", height=2,
                  command=close_command).pack(pady=20, padx=40, fill="x")

    def add_receipt_row(self, parent, label, value, is_total=False):
        font_label = ("Arial", 10, "bold" if is_total else "normal")
        font_val = ("Arial", 10, "bold" if is_total else "normal")
        color = "#1a1c3d" if is_total else "#666666"

        row = tk.Frame(parent, bg="#ffffff")
        row.pack(fill="x", pady=5)

        tk.Label(row, text=label, font=font_label, bg="#ffffff", fg="#999999").pack(side="left")
        tk.Label(row, text=value, font=font_val, bg="#ffffff", fg=color).pack(side="right")