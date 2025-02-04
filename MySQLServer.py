import mysql.connector
from mysql.connector import Error

# Database name
DB_NAME = "alx_book_store"

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host="localhost",  # Change to your MySQL host if needed
        user="root",       # Change to your MySQL username
        password="password"  # Change to your MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Create database (if it doesn't exist)
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME};")
        print(f"Database '{DB_NAME}' created successfully!")

except Error as e:
    print(f"Error: {e}")

finally:
    # Close cursor and connection safely
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
