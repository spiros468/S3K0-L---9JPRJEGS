import tkinter as tk
from tkinter import messagebox


class PaymentFormScreen:
    def __init__(self, root, method_type, amount, bill_id, on_success, back_command):
        self.root = root
        self.method_type = method_type  # "Debit" or "Credit"
        self.root.configure(bg="#ffffff")

        # --- Header ---
        header = tk.Frame(self.root, bg="#ffffff")
        header.pack(fill="x", pady=(20, 10))

        tk.Button(header, text="← Back", font=("Arial", 10), bg="white",
                  relief="flat", command=back_command).pack(side="left", padx=20)

        tk.Label(self.root, text=f"{method_type} Card Details",
                 font=("Arial", 16, "bold"), bg="#ffffff").pack(pady=20)

        # --- Form Container ---
        form_frame = tk.Frame(self.root, bg="#ffffff")
        form_frame.pack(padx=40, fill="x")

        # Input Fields
        #self.name_ent = self.create_input(form_frame, "Cardholder Name")
        self.card_ent = self.create_input(form_frame, "Card Number (16 digits)")

        # Expiry and CVV in one row
        row_frame = tk.Frame(form_frame, bg="#ffffff")
        row_frame.pack(fill="x", pady=10)

        self.expiry_ent = self.create_small_input(row_frame, "Expiry (MM/YY)", side="left")
        self.cvv_ent = self.create_small_input(row_frame, "CVV", side="right")

        # --- Submit Button ---
        tk.Button(self.root, text=f"Pay {amount}", font=("Arial", 12, "bold"),
                  bg="#28a745", fg="white", relief="flat", height=2,
                  command=lambda: self.validate_and_submit(on_success, bill_id)).pack(fill="x", padx=40, pady=40)

    def create_input(self, parent, label_text):
        tk.Label(parent, text=label_text, font=("Arial", 9), bg="#ffffff", fg="gray").pack(anchor="w", pady=(10, 2))
        ent = tk.Entry(parent, font=("Arial", 12), bd=1, relief="solid")
        ent.pack(fill="x", ipady=8)
        return ent

    def create_small_input(self, parent, label_text, side):
        container = tk.Frame(parent, bg="#ffffff")
        container.pack(side=side, fill="x", expand=True, padx=5)
        tk.Label(container, text=label_text, font=("Arial", 9), bg="#ffffff", fg="gray").pack(anchor="w")
        ent = tk.Entry(container, font=("Arial", 12), bd=1, relief="solid")
        ent.pack(fill="x", ipady=8)
        return ent

    def validate_and_submit(self, success_callback, bill_id):
        # Basic Validation Logic
        if len(self.card_ent.get()) < 16:
            messagebox.showerror("Error", "Please enter valid card details.")
            return

        # If valid, trigger the success logic in the Manager
        success_callback()