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

def create_tables(connection):
    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL
    );
    """

    create_expenses_table = """
    CREATE TABLE IF NOT EXISTS expenses (
        expense_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        category VARCHAR(50),
        amount DECIMAL(10, 2),
        date DATE,
        description TEXT,
        payment_method VARCHAR(50),                                                                                             FOREIGN KEY (user_id) REFERENCES users(user_id)                                                                     );
                                                                                                                            """
                                                                                                                            create_income_table = """
                                                                                                                            CREATE TABLE IF NOT EXISTS income (
                                                                                                                                income_id INT AUTO_INCREMENT PRIMARY KEY,
                                                                                                                                user_id INT,
                                                                                                                                source VARCHAR(50),
                                                                                                                                amount DECIMAL(10, 2),
                                                                                                                                date DATE,
                                                                                                                                FOREIGN KEY (user_id) REFERENCES users(user_id)
                                                                                                                            );
                                                                                                                            """
