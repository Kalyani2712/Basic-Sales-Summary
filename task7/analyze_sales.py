
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect("sales_data.db")

# SQL query to summarize sales
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product
"""

# Load query results into a pandas DataFrame
df = pd.read_sql_query(query, conn)

# Print full summary
print("🔹 Sales Summary by Product:")
print(df)

# Calculate KPIs
total_revenue = df['revenue'].sum()
total_qty = df['total_qty'].sum()
avg_price = total_revenue / total_qty

print(f"\n📈 Total Revenue: ₹{total_revenue:.2f}")
print(f"📦 Total Quantity Sold: {total_qty}")
print(f"💰 Average Selling Price: ₹{avg_price:.2f}")

# Show top 3 products by revenue
top_n = df.sort_values(by='revenue', ascending=False).head(3)
print("\n🏆 Top 3 Products by Revenue:")
print(top_n)

# Plot revenue by product (bar chart)
df.plot(kind='bar', x='product', y='revenue', legend=False, color='skyblue')
plt.title("Total Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("revenue_by_product.png")
plt.show()

# Plot quantity sold by product (bar chart)
df.plot(kind='bar', x='product', y='total_qty', legend=False, color='orange')
plt.title("Total Quantity Sold by Product")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.tight_layout()
plt.savefig("quantity_by_product.png")
plt.show()

# Plot revenue share (pie chart)
df.set_index('product')['revenue'].plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title("Revenue Share by Product")
plt.ylabel("")
plt.tight_layout()
plt.savefig("revenue_share_pie.png")
plt.show()

# Export summary to CSV
df.to_csv("sales_summary.csv", index=False)
print("\n✅ Summary exported to 'sales_summary.csv'")

# Close the database connection
conn.close()

'''
#Output : 

🔹 Sales Summary by Product:
      product  total_qty  revenue
0       Apple        128    362.8
1      Banana        112    235.8
2      Grapes        136    324.4
3       Mango        114    286.4
4      Orange        100    195.8
5       Peach        127    373.5
6   Pineapple        187    553.3
7  Strawberry        146    367.1

📈 Total Revenue: ₹2699.10
📦 Total Quantity Sold: 1050
💰 Average Selling Price: ₹2.57

🏆 Top 3 Products by Revenue:
      product  total_qty  revenue
6   Pineapple        187    553.3
5       Peach        127    373.5
7  Strawberry        146    367.1

✅ Summary exported to 'sales_summary.csv'

'''