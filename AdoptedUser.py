from User import User
import datetime
from Constants import *
import sqlite3
from sqlite3 import Error

# Find Adopted Users
class AdoptedUser(User):
    def __init__(self, signin_user, engagement_db):
        self.signed_in = signin_user
        self.engagement_db = engagement_db
        self.adopted_users = self.find_adopted_users(signin_user)
        self.save_adopted(self.adopted_users)
    
    # Get a list of adopted user & their beginning adopted dates
    def find_adopted_users(self, signed_in):
        l = []
        for user in signed_in:
            user_data = self.get_user_data(user)
            if len(user_data) < 3:
                continue
            else:
                adopted = self.helper_adopt(user_data[0], user_data[1], 
                                            user_data[2], user_data, 2)
                if (adopted != None):
                    l.append(adopted)
                    print(adopted)
        return l
    
    # Helper funciton to see if the user signed in 
    # 3 times consecutively a week. Return None if False
    def helper_adopt(self, first, second, third, user_data, i):
        format = '%Y-%m-%d %H:%M:%S'
        first_dt = datetime.datetime.strptime(first[1], format)
        third_dt = datetime.datetime.strptime(third[1], format)
        if (third_dt - first_dt <= datetime.timedelta(weeks = 1)):
            return (user_data[0][2], first[1])
        elif i == len(user_data) - 1:
            return None
        return self.helper_adopt(second, third, user_data[i + 1], 
                                 user_data, i + 1)
           
    # Query user data
    def get_user_data(self, user):
        query = "SELECT * FROM Engagement WHERE user_id == " + str(user)
        conn = self.create_connection(self.engagement_db)
        return self.execute_read_query(conn, query)
    
    # Save Adopted users to a SQL database
    def save_adopted(self, lst):
        conn = self.create_connection(ADOPT_DB)
        for adopted_user in lst:
            self.insert_data(conn, "Adopt", adopted_user)
        conn.close()






    
# Create a new table
def create_table():
    sql_create = """CREATE TABLE Adopt (
                object_id int,
                date_adopted varchar(40)
            );"""
    conn = sqlite3.connect(ADOPT_DB)
    cursor = conn.cursor()
    cursor.execute(sql_create)
    conn.commit()
    conn.close()

# def main():
#     conn = sqlite3.connect(ADOPT_DB)
#     cursor = conn.cursor()
#     for i in cursor.execute('SELECT * FROM Adopt'):
#         print(i)
#     conn.close()
    
# if __name__ == "__main__":
#     main()