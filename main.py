import tkinter as tk
from tkinter import ttk, messagebox

class BillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Billing System")
        self.root.geometry("500x500")

        self.items = []

        # --- Input Frame ---
        input_frame = tk.Frame(self.root, pady=10)
        input_frame.pack()

        tk.Label(input_frame, text="Item Name").grid(row=0, column=0, padx=10)
        self.item_name = tk.Entry(input_frame)
        self.item_name.grid(row=0, column=1)

        tk.Label(input_frame, text="Price").grid(row=1, column=0, padx=10)
        self.price = tk.Entry(input_frame)
        self.price.grid(row=1, column=1)

        tk.Label(input_frame, text="Quantity").grid(row=2, column=0, padx=10)
        self.quantity = tk.Entry(input_frame)
        self.quantity.grid(row=2, column=1)

        tk.Button(input_frame, text="Add Item", command=self.add_item).grid(row=3, columnspan=2, pady=10)

        # --- Bill Area ---
        self.bill_area = tk.Text(self.root, width=60, height=15, borderwidth=2, relief='sunken')
        self.bill_area.pack(pady=10)
        self.bill_area.insert(tk.END, "====== Bill ======\n")

        # --- Total Button ---
        tk.Button(self.root, text="Calculate Total", command=self.calculate_total).pack(pady=5)

    def add_item(self):
        name = self.item_name.get().strip()

        # Try converting price & quantity to floats (>0)
        try:
            price = float(self.price.get())
            qty   = float(self.quantity.get())
            if price <= 0 or qty <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror(
                "Input Error",
                "Price and quantity must be numbers greater than 0 "
                "(decimals allowed, e.g., 12.5 or 0.75)."
            )
            return

        total = price * qty
        self.items.append((name, price, qty, total))

        # g‑format avoids trailing zeros (shows 1.5, not 1.500000)
        self.bill_area.insert(
            tk.END,
            f"{name or 'Unnamed'} - {qty:g} x {price:g} = {total:.2f}\n"
        )

        # Clear inputs
        self.item_name.delete(0, tk.END)
        self.price.delete(0, tk.END)
        self.quantity.delete(0, tk.END)

    def calculate_total(self):
        if not self.items:
            messagebox.showinfo("No Items", "Add items before calculating total.")
            return

        grand_total = sum(item[3] for item in self.items)
        self.bill_area.insert(tk.END, f"\nTotal Amount: ₹{grand_total:.2f}\n")
        self.bill_area.insert(tk.END, "===================\n")

# --- Run App ---
if __name__ == "__main__":
    root = tk.Tk()
    app = BillingApp(root)
    root.mainloop()
