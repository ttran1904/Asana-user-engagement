import sqlite3 
import pandas as pd 
from SignInUser import SignInUser
from AdoptedUser import AdoptedUser
from Constants import *

# Main controller to manipulate lower functions to find data

class Processor():
    def __init__(self):
        self.d = None

    # Convert a csv file to sql DB file
    def csv_to_sql(self, db_name, csv_path, sql_path):
        conn = sqlite3.connect(sql_path)
        data = pd.read_csv(csv_path, encoding="ISO-8859-1")
        data.to_sql(db_name, conn, if_exists = 'replace')
    
    # Print out the contents of a DB file
    def cursor(self, db_name, sql_path):
        conn = sqlite3.connect(sql_path)
        cur = conn.cursor() 
        for row in cur.execute('SELECT * FROM ' + db_name): 
            print(row) 
        conn.close() 

# Read the Engagement file
def read_engagement_csv():
    p = Processor()
    p.csv_to_sql("Engagement", ENGAGEMENT_CSV, ENGAGEMENT_DB)
    p.cursor("Engagement", ENGAGEMENT_DB)

# Read the User file
def read_user_csv():
    p = Processor()
    p.csv_to_sql("User", USER_CSV, USER_DB)
    p.cursor("User", USER_DB)

def main():
    signed_in = SignInUser(USER_DB)
    AdoptedUser(signed_in.users, ENGAGEMENT_DB)

if __name__ == "__main__":
    main()
