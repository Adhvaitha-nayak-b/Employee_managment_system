# Define global variables for cursor and connection
import mysql
from mysql.connector import connect, Error
#from sqlite3 import connect

from fullcode import create_table, insert_data_from_csv

cursor = None
connection = None

def mysql_connect(host, user, password, database):
    global connection  # Declare connection as a global variable
    try:
        connection = connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection  # Return the connection object
        else:
            print("Failed to connect to MySQL")
            return None
    except Error as e:
        print(f"Error connecting to MySQL : {e}")
        return None
def main():
    host = "127.0.0.1"
    user = "root"
    password = "nineleaps"
    database = "new"

    # Connect to MySQL database
    connection = connect_to_mysql(host, user, password, database)
    if connection:
        create_table(connection)
       # insert_data_from_csv(connection, '/home/nineleaps/Downloads/all.csv')
