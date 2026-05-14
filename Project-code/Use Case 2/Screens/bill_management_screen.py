import tkinter as tk
from tkinter import ttk, messagebox

class BillingDashboard:
    def __init__(self, root, data, on_select=None):
        self.root = root
        self.root.title("Bill Screen")
        self.root.geometry("900x400")
        self.data = data
        self.on_select = on_select

        # --- Title and Search Bar ---
        top_frame = tk.Frame(root)
        top_frame.pack(fill="x", padx=10, pady=10)

        tk.Label(top_frame, text="Billing History", font=("Arial", 14, "bold")).pack(side="left")

        #search_btn = tk.Button(top_frame, text="🔍 Search...", state="disabled")
        #search_btn.pack(side="right")

        # --- The Table (Treeview) ---
        # Define columns
        columns = ("date", "bill_id", "status", "amount")

        self.tree = ttk.Treeview(root, columns=columns, show="headings", height=10)

        # Define Headings
        self.tree.heading("date", text="Date ↑")
        self.tree.heading("bill_id", text="Bill ID")
        #self.tree.heading("recipient", text="Recipient")
        self.tree.heading("status", text="Status")
        self.tree.heading("amount", text="Final Amount")

        # Define Column Widths
        self.tree.column("date", width=100)
        self.tree.column("bill_id", width=100)
        #self.tree.column("recipient", width=250)
        self.tree.column("status", width=120, anchor="center")
        self.tree.column("amount", width=120, anchor="e") # East (right) align for currency

        # Sample Data (Matching your screenshot)



        # Add data to the tree
        for i in range(self.data.shape[0]):
            self.tree.insert("", tk.END, values=tuple(self.data[i]))

        self.tree.pack(fill="both", expand=True, padx=10, pady=5)

        # --- Bottom Info ---
        tk.Label(root, text="Showing 1 to 5 of 5 entries", fg="gray").pack(side="left", padx=10)

        self.tree.bind("<Double-1>", self._on_double_click)


    def _on_double_click(self, event):
        item_id = self.tree.focus()
        values = self.tree.item(item_id)['values']

        if values and self.on_select:
            # Send the Bill ID (index 1) back to the Manager
            bill_id = values[1]
            self.on_select(bill_id)


# Styling the Treeview to look cleaner
def apply_style():
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
    style.configure("Treeview", rowheight=30)

