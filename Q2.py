class SalesDatabase:
    def __init__(self):
        self.sales_data = []

    def record_sale(self, customer_name, purchased_items, purchase_date):
        self.sales_data.append({'customer_name': customer_name, 'purchased_items': purchased_items, 'purchase_date': purchase_date})

    def calculate_total_sales(self, start_date, end_date):
        total_sales = 0
        for sale in self.sales_data:
            if start_date <= sale['purchase_date'] <= end_date:
                total_sales += sum(item['price'] for item in sale['purchased_items'])
        return total_sales

    def generate_customer_report(self):
        customer_sales = {}
        for sale in self.sales_data:
            customer_name = sale['customer_name']
            if customer_name not in customer_sales:
                customer_sales[customer_name] = 0
            customer_sales[customer_name] += sum(item['price'] for item in sale['purchased_items'])
        return customer_sales

# Example usage:
sales_db = SalesDatabase()
sales_db.record_sale("Customer A", [{"item": "Product A", "price": 10.99}], "2023-10-18")
sales_db.record_sale("Customer B", [{"item": "Product B", "price": 5.99}], "2023-10-19")
total_sales = sales_db.calculate_total_sales("2023-10-01", "2023-10-31")
customer_sales = sales_db.generate_customer_report()
print(f"Total Sales: ${total_sales}")
print("Customer Sales:")
for customer, sales in customer_sales.items():
    print(f"{customer}: ${sales}")
