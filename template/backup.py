import subprocess
import os

# Database connection parameters
DB_USER = 'postgres'
DB_PASSWORD = 'm4st3r'
DB_HOST = '192.168.64.23'
DB_PORT = '5432'
DB_NAME = 'mycompany'
BACKUP_FILE = 'mycompany_backup.backup'

# Set the PGPASSWORD environment variable to avoid password prompt
os.environ['PGPASSWORD'] = DB_PASSWORD

# Run the pg_dump command
try:
    subprocess.run(
        [
            'pg_dump',
            '-h', DB_HOST,
            '-p', DB_PORT,
            '-U', DB_USER,
            '-f', BACKUP_FILE,
            DB_NAME
        ],
        check=True
    )
    print(f"Backup of database '{DB_NAME}' created successfully as '{BACKUP_FILE}'")
except subprocess.CalledProcessError as e:
    print(f"Error occurred during backup: {e}")

# Clean up the PGPASSWORD environment variable
del os.environ['PGPASSWORD']
