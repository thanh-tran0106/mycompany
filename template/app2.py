import pandas as pd
from sqlalchemy import create_engine

# Define your PostgreSQL database credentials
user = 'postgres'
password = 'm4st3r'
host = '192.168.64.23'
port = '5432'
database = 'mycompany'

# Create a connection string
connection_string = f'postgresql://{user}:{password}@{host}:{port}/{database}'

# Create a database engine
engine = create_engine(connection_string)

# Load data from tables into DataFrames
df_products = pd.read_sql('SELECT * FROM products', engine)
df_orders = pd.read_sql('SELECT * FROM orders', engine)

# Filter orders for a specific product
product_name = 'Laptop'
df_filtered_orders = df_orders[df_orders['product_id'].isin(df_products[df_products['category'] == product_name]['product_id'])]

# Calculate total number of orders and total revenue for the filtered product
total_orders = df_filtered_orders.shape[0]
total_revenue = df_filtered_orders['price'].sum()

print(f"Total number of orders for {product_name}: {total_orders}")
print(f"Total revenue for {product_name}: ${total_revenue:.2f}")
