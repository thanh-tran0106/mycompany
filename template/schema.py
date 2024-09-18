import psycopg2
from psycopg2 import sql

# Define your PostgreSQL database credentials
user = 'postgres'
password = 'm4st3r'
host = '192.168.64.23'
port = '5432'
database = 'mycompany'
conn = psycopg2.connect(
    host=host,
    port=port,
    dbname=database,
    user=user,
    password=password
)

# Create a cursor object
cur = conn.cursor()

# Define data to be inserted

data = {
    'tenant2': {
        'products': [
            ('Smartphone', 'Electronics', 500.00),
            ('Keyboard', 'Accessories', 75.00),
        ],
        'customers': [
            ('Charlie', 'UK'),
            ('Diana', 'Australia'),
        ],
        'orders': [
            (1, '2024-09-20', 1, 3),
            (2, '2024-09-21', 2, 2),
        ]
    },
    'tenant3': {
        'products': [
            ('Tablet', 'Electronics', 300.00),
            ('Headphones', 'Accessories', 85.00),
        ],
        'customers': [
            ('Edward', 'Germany'),
            ('Fiona', 'France'),
        ],
        'orders': [
            (1, '2024-09-22', 1, 1),
            (2, '2024-09-23', 2, 4),
        ]
    }
}

# Function to insert data into a schema
def insert_data(schema_name, table_name, rows):
    try:
        # Adjust query for each table
        if table_name == 'products':
            insert_query = sql.SQL("INSERT INTO {}.{} (product_name, category, price) VALUES (%s, %s, %s)").format(
                sql.Identifier(schema_name),
                sql.Identifier(table_name)
            )
        elif table_name == 'customers':
            insert_query = sql.SQL("INSERT INTO {}.{} (customer_name, country) VALUES (%s, %s)").format(
                sql.Identifier(schema_name),
                sql.Identifier(table_name)
            )
        elif table_name == 'orders':
            insert_query = sql.SQL("INSERT INTO {}.{} (customer_id, order_date, product_id, quantity) VALUES (%s, %s, %s, %s)").format(
                sql.Identifier(schema_name),
                sql.Identifier(table_name)
            )
        else:
            raise ValueError("Unknown table name")

        cur.executemany(insert_query, rows)
        print(f"Data inserted into {schema_name}.{table_name}")
    except Exception as e:
        print(f"Error inserting data into {schema_name}.{table_name}: {e}")

# Insert data for each tenant
for tenant, tables in data.items():
    for table_name, rows in tables.items():
        insert_data(tenant, table_name, rows)


# Commit changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

print ("Data insertion complete.")