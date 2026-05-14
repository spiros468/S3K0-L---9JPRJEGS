import tkinter as tk

class PaymentMethodScreen:
    def __init__(self, root, amount, back_command, on_debit, on_credit):
        self.root = root
        self.root.configure(bg="#ffffff")

        # --- Header ---
        header = tk.Frame(self.root, bg="#ffffff")
        header.pack(fill="x", pady=(20, 10))

        # Simple back button to return to Bill Details
        tk.Button(header, text="← Back", font=("Arial", 10), bg="white",
                  relief="flat", command=back_command).pack(side="left", padx=20)

        # --- Content Area ---
        tk.Label(self.root, text="Choose Payment Method", font=("Arial", 16, "bold"),
                 bg="#ffffff", fg="#1a1c3d").pack(pady=(30, 5))

        tk.Label(self.root, text=f"Total Amount: {amount}", font=("Arial", 12),
                 bg="#ffffff", fg="#666").pack(pady=(0, 40))

        # --- Payment Options (The "Cards") ---
        # We wrap these in a frame to control the width
        options_frame = tk.Frame(self.root, bg="#ffffff")
        options_frame.pack(padx=50, fill="x")

        # Debit Card Option
        self.create_method_button(options_frame, "Debit Card", "💳", on_debit)

        # Small Spacer
        tk.Frame(options_frame, height=15, bg="#ffffff").pack()

        # Credit Card Option
        self.create_method_button(options_frame, "Credit Card", "🪪", on_credit)

    def create_method_button(self, parent, text, icon, command):
        """Creates a stylized button that looks like a selectable card."""
        btn = tk.Button(
            parent,
            text=f"{icon}   {text}",
            font=("Arial", 12, "bold"),
            bg="#f9f9f9",
            fg="#1a1c3d",
            activebackground="#ececec",
            relief="solid",
            bd=1,
            height=3,
            command=command
        )
        btn.pack(fill="x", pady=5)

    def process_debit(self):
        print("Processing Debit Card...")
        # Add your debit logic here

    def process_credit(self):
        print("Processing Credit Card...")
        # Add your credit logic here