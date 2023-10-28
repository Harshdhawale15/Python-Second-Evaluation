import tkinter as tk

class StoreGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Store Interface")

        self.product_label = tk.Label(root, text="Product:")
        self.product_label.pack()
        self.product_entry = tk.Entry(root)
        self.product_entry.pack()

        self.add_button = tk.Button(root, text="Add to Cart", command=self.add_to_cart)
        self.add_button.pack()

        self.cart_label = tk.Label(root, text="Shopping Cart:")
        self.cart_label.pack()

        self.cart = []
        self.cart_display = tk.Label(root, text="")
        self.cart_display.pack()

        self.calculate_button = tk.Button(root, text="Calculate Total", command=self.calculate_total)
        self.calculate_button.pack()

        self.total_label = tk.Label(root, text="")
        self.total_label.pack()

    def add_to_cart(self):
        product = self.product_entry.get()
        self.cart.append(product)
        self.cart_display.config(text="\n".join(self.cart))
        self.product_entry.delete(0, tk.END)

    def calculate_total(self):
        total_cost = 0  # Calculate the total cost based on the products in the cart.
        self.total_label.config(text=f"Total Cost: ${total_cost}")

root = tk.Tk()
app = StoreGUI(root)
root.mainloop()
