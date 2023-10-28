import pandas as pd
import matplotlib.pyplot as plt

# Load sales data from a CSV file
sales_data = pd.read_csv('sales_data.csv')

# Analyze sales trends over time
sales_data['purchase_date'] = pd.to_datetime(sales_data['purchase_date'])
sales_data.set_index('purchase_date', inplace=True)
monthly_sales = sales_data['price'].resample('M').sum()

# Create a line chart to visualize monthly sales trends
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.title('Monthly Sales Trends')
plt.show()

# Identify peak sales hours and popular products
hourly_sales = sales_data['price'].groupby(sales_data.index.hour).sum()
popular_products = sales_data['product'].value_counts()

# Generate reports for store management
print("Peak Sales Hours:")
print(hourly_sales)

print("Popular Products:")
print(popular_products)
