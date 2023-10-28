class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name, quantity, price):
        self.inventory[item_name] = {'quantity': quantity, 'price': price}

    def update_item(self, item_name, quantity, price):
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] = quantity
            self.inventory[item_name]['price'] = price

    def remove_item(self, item_name):
        if item_name in self.inventory:
            del self.inventory[item_name]

    def generate_report(self):
        for item, details in self.inventory.items():
            print(f"Item: {item}, Quantity: {details['quantity']}, Price: {details['price']}")

# Example usage:
inventory = Inventory()
inventory.add_item("Product A", 100, 10.99)
inventory.add_item("Product B", 50, 5.99)
inventory.update_item("Product A", 80, 12.99)
inventory.remove_item("Product B")
inventory.generate_report()
