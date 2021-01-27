import sqlite3
from sqlite3 import Error

# Connect to a User Database (User DB or Engagement DB)
class User():
    def __init__(self):
        return
    
    # Create connection to the Engagement DB
    def create_connection(self, path):
        connection = None
        try:
            connection = sqlite3.connect(path)
            print("Connection to SQLite DB successful")
            return connection
        except Error as e:
            print(f"The error '{e}' occurred")
            return connection

    # Read query from SQL CONNECTION and a string QUERY
    def execute_read_query(self, connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")
    
    # Insert a data into a SQL table
    def insert_data(self, conn, table_name, tuple_data):
        insert = "INSERT INTO "+ table_name +" VALUES " + str(tuple_data) + ";"
        cursor = conn.cursor()
        cursor.execute(insert)
        conn.commit()