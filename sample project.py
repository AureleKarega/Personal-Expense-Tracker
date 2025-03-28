import mysql.connector
from mysql.connector import Error
from prettytable import PrettyTable
import getpass

# Function to create a connection to the MySQL database
def create_conn():
    conn = None
    try:
        conn = mysql.connector.connect(
            host='01e489f6c6f8.1009380b.alu-cod.online',  # Replace with your host
            port='37443',
            database='sample',  # Replace with your database name
            user='attorney',    # Replace with your username
            password='1234'     # Replace with your password
        )
        if conn.is_connected():
            print('Connected to MySQL database')
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    return conn