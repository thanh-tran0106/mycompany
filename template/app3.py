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

# Load data from a table into a DataFrame
df_products = pd.read_sql('SELECT * FROM products', engine)

# Example of updating a price for a product
product_id = '4'
new_price = 1099

# Update the price in the DataFrame
df_products.loc[df_products['product_id'] == product_id, 'price'] = new_price

# Write the updated DataFrame back to PostgreSQL
df_products.to_sql('products', engine, if_exists='replace', index=False)

print("Price updated successfully!")
