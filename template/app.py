import pandas as pd
from sqlalchemy import create_engine

#Define your PostgreSQL database credentials
user = 'postgres'
password = 'm4st3r'
host = '192.168.64.23'
port = '5432'
database = 'mycompany'

# create a connection string
connection_string = f'postgresql://{user}:{password}@{host}:{port}/{database}'

# Create a database engine
engine = create_engine(connection_string)

#Load data from tables into DataFrames
df_products = pd.read_sql('SELECT * FROM products', engine)
df_orders = pd.read_sql('SELECT * FROM orders', engine)

#Merge DataFrames on ProductID
df_merged = pd.merge(df_orders, df_products, on='product_id')

#Caculate total revenue per product
df_report = df_merged.groupby('category')['price'].sum().reset_index()

print("Report - Total Revenue per Product:")
print(df_report)
