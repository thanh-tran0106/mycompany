import psycopg2
from psycopg2 import sql

# Database connection parameters
user = 'postgres'
password = 'm4st3r'
host = '192.168.64.23'
port = '5432'
database = 'mycompany'

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host=host,
    port=port,
    dbname=database,
    user=user,
    password=password
)

# Create a cursor object
cur = conn.cursor()

# Define the SQL statements to create tables
create_tables = {
    'tenant2': {
        'products': """
            CREATE TABLE tenant2.products (
                product_id SERIAL PRIMARY KEY,
                product_name VARCHAR(100) NOT NULL,
                category VARCHAR(50) NOT NULL,
                price NUMERIC(10, 2) NOT NULL
            );
        """,
        'customers': """
            CREATE TABLE tenant2.customers (
                customer_id SERIAL PRIMARY KEY,
                customer_name VARCHAR(100) NOT NULL,
                country VARCHAR(50) NOT NULL
            );
        """,
        'orders': """
            CREATE TABLE tenant2.orders (
                order_id SERIAL PRIMARY KEY,
                customer_id INT REFERENCES tenant2.customers(customer_id),
                order_date DATE NOT NULL,
                product_id INT REFERENCES tenant2.products(product_id),
                quantity INT NOT NULL
            );
        """
    },
    'tenant3': {
        'products': """
            CREATE TABLE tenant3.products (
                product_id SERIAL PRIMARY KEY,
                product_name VARCHAR(100) NOT NULL,
                category VARCHAR(50) NOT NULL,
                price NUMERIC(10, 2) NOT NULL
            );
        """,
        'customers': """
            CREATE TABLE tenant3.customers (
                customer_id SERIAL PRIMARY KEY,
                customer_name VARCHAR(100) NOT NULL,
                country VARCHAR(50) NOT NULL
            );
        """,
        'orders': """
            CREATE TABLE tenant3.orders (
                order_id SERIAL PRIMARY KEY,
                customer_id INT REFERENCES tenant3.customers(customer_id),
                order_date DATE NOT NULL,
                product_id INT REFERENCES tenant3.products(product_id),
                quantity INT NOT NULL
            );
        """
    }
}

# Function to execute table creation SQL statements
def create_tables_for_tenant(schema_name, table_definitions):
    for table_name, create_statement in table_definitions.items():
        try:
            cur.execute(create_statement)
            print(f"Table {schema_name}.{table_name} created successfully.")
        except Exception as e:
            print(f"Error creating table {schema_name}.{table_name}: {e}")

# Create tables for each tenant
for tenant, tables in create_tables.items():
    create_tables_for_tenant(tenant, tables)

# Commit changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

print("All tables created successfully.")
