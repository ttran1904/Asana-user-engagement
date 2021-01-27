from Constants import *
import sqlite3
from sqlite3 import Error

# Analyzer class on adopted-users
class Analyzer():
    def __init__(self):
        self._source = ("PERSONAL_PROJECTS", 
                        "GUEST_INVITE", 
                        "ORG_INVITE", 
                        "SIGNUP", 
                        "SIGNUP_GOOGLE_AUTH")
        return
    
    # Analyze creation source
    def analyze_source(self):
        conn = sqlite3.connect(ADOPT_DB)
        cursor = conn.cursor()
        
        for s in self._source:
            success = cursor.execute("""SELECT COUNT(*) FROM User INNER JOIN Adopt 
                                ON User.object_id == Adopt.object_id
                                WHERE creation_source == ?""", 
                                (s,)).fetchone()[0]
            total = cursor.execute("""SELECT COUNT(*) FROM User
                                WHERE creation_source == ?""", (s,)).fetchone()[0]
            rate = success / total * 100
            print("Invites from {0} has {1} adopted-users in a total of {2} sign-in users. Rate: {3}% "
                  .format(s, success, total, rate))
        conn.close()
    
    # Analyze mailing percentage in adopted-users.
    def analyze_mailing_in_adopted(self):
        conn = sqlite3.connect(ADOPT_DB)
        cursor = conn.cursor()
        
        success = cursor.execute("""SELECT COUNT(*) FROM User INNER JOIN Adopt 
                                ON User.object_id == Adopt.object_id 
                                WHERE opted_in_to_mailing_list == 1""").fetchone()[0]
        total = cursor.execute("""SELECT COUNT(*) FROM User INNER JOIN Adopt 
                                ON User.object_id == Adopt.object_id""").fetchone()[0]
        rate = success / total * 100
        print("{0} adopted-users opted into mailing in a total of {1} sign-in users. Rate: {2}% "
                  .format(success, total, rate))
        conn.close()
    
    # Analyze marketing drip percentage in adopted-users.
    def analyze_marketing_in_adopted(self):
        conn = sqlite3.connect(ADOPT_DB)
        cursor = conn.cursor()
        
        success = cursor.execute("""SELECT COUNT(*) FROM User INNER JOIN Adopt 
                                ON User.object_id == Adopt.object_id 
                                WHERE enabled_for_marketing_drip == 1""").fetchone()[0]
        total = cursor.execute("""SELECT COUNT(*) FROM User INNER JOIN Adopt 
                                ON User.object_id == Adopt.object_id""").fetchone()[0]
        rate = success / total * 100
        print("{0} adopted-users has marketing drip in a total of {1} sign-in users. Rate: {2}% "
                  .format(success, total, rate))
        conn.close()
    
    # Analyze invited percentage in adopted
    def analyze_invited_in_adopted(self):
        conn = sqlite3.connect(ADOPT_DB)
        cursor = conn.cursor()
        
        success = cursor.execute("""SELECT COUNT(*) FROM User INNER JOIN Adopt 
                                ON User.object_id == Adopt.object_id 
                                WHERE invited_by_user_id != "None" """).fetchone()[0]
        total = cursor.execute("""SELECT COUNT(*) FROM User INNER JOIN Adopt 
                                ON User.object_id == Adopt.object_id""").fetchone()[0]
        rate = success / total * 100
        print("{0} adopted-users was invited by someone in a total of {1} sign-in users. Rate: {2}% "
                  .format(success, total, rate))
        conn.close()
    
    # Analyze insolated percentage in adopted
    def analyze_isolated_in_adopted(self):
        conn = sqlite3.connect(ADOPT_DB)
        cursor = conn.cursor()
        
        success = cursor.execute("""SELECT COUNT(*) FROM User INNER JOIN Adopt 
                                ON User.object_id == Adopt.object_id 
                                WHERE invited_by_user_id == "None" 
                                    AND enabled_for_marketing_drip == 0
                                    AND opted_in_to_mailing_list == 0""").fetchone()[0]
        total = cursor.execute("""SELECT COUNT(*) FROM User INNER JOIN Adopt 
                                ON User.object_id == Adopt.object_id""").fetchone()[0]
        rate = success / total * 100
        print("{0} adopted-users was isolated in a total of {1} sign-in users. Rate: {2}% "
                  .format(success, total, rate))
        conn.close()

    # Analyze organizations in adopted
    def analyze_org_in_adopted(self):
        conn = sqlite3.connect(ADOPT_DB)
        cursor = conn.cursor()
        
        success = cursor.execute("""SELECT COUNT(*) FROM User INNER JOIN Adopt 
                                ON User.object_id == Adopt.object_id 
                                WHERE org_id != "None" """).fetchone()[0]
        total = cursor.execute("""SELECT COUNT(*) FROM User INNER JOIN Adopt 
                                ON User.object_id == Adopt.object_id""").fetchone()[0]
        rate = success / total * 100
        print("{0} adopted-users are in an organization in a total of {1} sign-in users. Rate: {2}% "
                  .format(success, total, rate))
        conn.close()

    # Analyze invite transfer rate
    def analyze_invite_transfer(self):
        conn = sqlite3.connect(ADOPT_DB)
        cursor = conn.cursor()
        
        success = cursor.execute("""SELECT COUNT(*) FROM User INNER JOIN Adopt 
                                ON User.object_id == Adopt.object_id
                                WHERE invited_by_user_id != "None" """).fetchone()[0]
        total = cursor.execute("""SELECT COUNT(*) FROM User 
                               WHERE invited_by_user_id != "None" 
                               AND last_session_creation_time != "None" """).fetchone()[0]
        rate = success / total * 100
        print("{0} users adopted after invitation in a total of {1} sign-in users. Rate: {2}% "
                  .format(success, total, rate))
        conn.close()
    
    # Analyze mailing transfer rate
    def analyze_mailing_transfer(self):
        conn = sqlite3.connect(ADOPT_DB)
        cursor = conn.cursor()
        
        success = cursor.execute("""SELECT COUNT(*) FROM User INNER JOIN Adopt 
                                ON User.object_id == Adopt.object_id
                                WHERE opted_in_to_mailing_list == 1 """).fetchone()[0]
        total = cursor.execute("""SELECT COUNT(*) FROM User 
                               WHERE opted_in_to_mailing_list == 1
                               AND last_session_creation_time != "None" """).fetchone()[0]
        rate = success / total * 100
        print("{0} users adopted after opted into mail in a total of {1} sign-in users. Rate: {2}% "
                  .format(success, total, rate))
        conn.close()
    
    # Analyze mailing transfer rate
    def analyze_marketing_transfer(self):
        conn = sqlite3.connect(ADOPT_DB)
        cursor = conn.cursor()
        
        success = cursor.execute("""SELECT COUNT(*) FROM User INNER JOIN Adopt 
                                ON User.object_id == Adopt.object_id
                                WHERE enabled_for_marketing_drip == 1 """).fetchone()[0]
        total = cursor.execute("""SELECT COUNT(*) FROM User 
                               WHERE enabled_for_marketing_drip == 1
                               AND last_session_creation_time != "None" """).fetchone()[0]
        rate = success / total * 100
        print("{0} users adopted with marketing drip in a total of {1} sign-in users. Rate: {2}% "
                  .format(success, total, rate))
        conn.close()

    # Analyze combination of mailing, marketing, and invite transfer rate
    def analyze_combine_transfer(self):
        conn = sqlite3.connect(ADOPT_DB)
        cursor = conn.cursor()

        success = cursor.execute("""SELECT COUNT(*) FROM User INNER JOIN Adopt 
                                ON User.object_id == Adopt.object_id
                                WHERE enabled_for_marketing_drip == 1 
                                AND opted_in_to_mailing_list == 1 """).fetchone()[0]
        total = cursor.execute("""SELECT COUNT(*) FROM User 
                               WHERE enabled_for_marketing_drip == 1
                               AND opted_in_to_mailing_list == 1
                               AND last_session_creation_time != "None" """).fetchone()[0]
        rate = success / total * 100
        print("{0} users adopted with mailing & marketing in a total of {1} sign-in users. Rate: {2}% "
                  .format(success, total, rate))
        
        success = cursor.execute("""SELECT COUNT(*) FROM User INNER JOIN Adopt 
                                ON User.object_id == Adopt.object_id
                                WHERE invited_by_user_id != "None"
                                AND opted_in_to_mailing_list == 1 """).fetchone()[0]
        total = cursor.execute("""SELECT COUNT(*) FROM User 
                               WHERE invited_by_user_id != "None"
                               AND opted_in_to_mailing_list == 1
                               AND last_session_creation_time != "None" """).fetchone()[0]
        rate = success / total * 100
        print("{0} users adopted with mailing & invite in a total of {1} sign-in users. Rate: {2}% "
                  .format(success, total, rate))
        
        success = cursor.execute("""SELECT COUNT(*) FROM User INNER JOIN Adopt 
                                ON User.object_id == Adopt.object_id
                                WHERE invited_by_user_id != "None"
                                AND enabled_for_marketing_drip == 1 """).fetchone()[0]
        total = cursor.execute("""SELECT COUNT(*) FROM User 
                               WHERE invited_by_user_id != "None"
                               AND enabled_for_marketing_drip == 1
                               AND last_session_creation_time != "None" """).fetchone()[0]
        rate = success / total * 100
        print("{0} users adopted with marketing & invite in a total of {1} sign-in users. Rate: {2}% "
                  .format(success, total, rate))
        
        success = cursor.execute("""SELECT COUNT(*) FROM User INNER JOIN Adopt 
                                ON User.object_id == Adopt.object_id
                                WHERE invited_by_user_id != "None"
                                AND opted_in_to_mailing_list == 1
                                AND enabled_for_marketing_drip == 1 """).fetchone()[0]
        total = cursor.execute("""SELECT COUNT(*) FROM User 
                               WHERE invited_by_user_id != "None"
                               AND opted_in_to_mailing_list == 1
                               AND enabled_for_marketing_drip == 1
                               AND last_session_creation_time != "None" """).fetchone()[0]
        rate = success / total * 100
        print("{0} users adopted with mailing & marketing & invite in a total of {1} sign-in users. Rate: {2}% "
                  .format(success, total, rate))
        conn.close()

    # Analyze organization transfer rate
    def analyze_org_transfer(self):
        conn = sqlite3.connect(ADOPT_DB)
        cursor = conn.cursor()
        success = cursor.execute("""SELECT COUNT(*) FROM User INNER JOIN Adopt 
                                ON User.object_id == Adopt.object_id
                                WHERE org_id != "None" """).fetchone()[0]
        total = cursor.execute("""SELECT COUNT(*) FROM User 
                               WHERE org_id != "None"
                               AND last_session_creation_time != "None" """).fetchone()[0]
        rate = success / total * 100
        print("{0} users adopted from organizations in a total of {1} sign-in users. Rate: {2}% "
                  .format(success, total, rate))
        conn.close()
    
    # Analyze combine organization transfer rate with the 3 others
    def analyze_org_combine_transfer(self): 
        conn = sqlite3.connect(ADOPT_DB)
        cursor = conn.cursor()
        success = cursor.execute("""SELECT COUNT(*) FROM User INNER JOIN Adopt 
                                ON User.object_id == Adopt.object_id
                                WHERE org_id != "None" 
                                AND opted_in_to_mailing_list == 1""").fetchone()[0]
        total = cursor.execute("""SELECT COUNT(*) FROM User 
                               WHERE org_id != "None"
                               AND opted_in_to_mailing_list == 1
                               AND last_session_creation_time != "None" """).fetchone()[0]
        rate = success / total * 100
        print("{0} users adopted from organizations & mail in a total of {1} sign-in users. Rate: {2}% "
                  .format(success, total, rate))
        
        success = cursor.execute("""SELECT COUNT(*) FROM User INNER JOIN Adopt 
                                ON User.object_id == Adopt.object_id
                                WHERE org_id != "None" 
                                AND invited_by_user_id != "None"
                                AND opted_in_to_mailing_list == 1
                                AND enabled_for_marketing_drip == 1""").fetchone()[0]
        total = cursor.execute("""SELECT COUNT(*) FROM User 
                               WHERE org_id != "None"
                               AND invited_by_user_id != "None"
                               AND opted_in_to_mailing_list == 1
                               AND enabled_for_marketing_drip == 1
                               AND last_session_creation_time != "None" """).fetchone()[0]
        rate = success / total * 100
        print("{0} users adopted from organizations & mail & marketing & invite in a total of {1} sign-in users. Rate: {2}% "
                  .format(success, total, rate))
        conn.close()
    
    # Find distinct email domains
    def distinct_email(self):
        conn = sqlite3.connect(ADOPT_DB)
        cursor = conn.cursor()
        l = []
        for i in cursor.execute("""SELECT DISTINCT email_domain FROM User """):
            l.append(i[0])
        conn.close()
        return l
    
    # Analyze emails in adopted
    def analyze_email_adopted(self):
        conn = sqlite3.connect(ADOPT_DB)
        cursor = conn.cursor()
        
        total = cursor.execute("""SELECT COUNT(*) FROM User INNER JOIN Adopt 
                                ON User.object_id == Adopt.object_id""").fetchone()[0]
        for i in cursor.execute(""" SELECT email_domain, COUNT(*) FROM User INNER JOIN Adopt 
                                ON User.object_id == Adopt.object_id
                                GROUP BY email_domain
                                ORDER BY COUNT(*) DESC LIMIT 6"""):
            percent = i[1] / total * 100
            print("{0} {1} users are in the total {2} adopted group. Percent: {3}%"
                  .format(i[1], i[0], total, percent))
        conn.close()
        
    # Analyze emails in signed in
    def analyze_email_signin(self):
        conn = sqlite3.connect(ADOPT_DB)
        cursor = conn.cursor()
        
        total = cursor.execute("""SELECT COUNT(*) FROM User 
                               WHERE last_session_creation_time != "None" """).fetchone()[0]
        for i in cursor.execute(""" SELECT email_domain, COUNT(*) FROM User 
                                WHERE last_session_creation_time != "None"
                                GROUP BY email_domain
                                ORDER BY COUNT(*) DESC LIMIT 6"""):
            percent = i[1] / total * 100
            print("{0} {1} users are in the total {2} signin group. Percent: {3}%"
                  .format(i[1], i[0], total, percent))
        conn.close()

def copy_db(src, dest):
    conn1 = sqlite3.connect(src)
    conn2 = sqlite3.connect(dest)
    cursor1 = conn1.cursor()
    cursor2 = conn2.cursor()

    for i in cursor1.execute('SELECT * FROM User'):
        params = (i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11])
        cursor2.execute("""INSERT INTO User VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", params)
    conn2.commit()
    conn1.close()


# Create a new table
def create_table():
    sql_create = """CREATE TABLE User (
                "index" int,
                object_id int,
                creation_time varchar(40),
                name varchar(225),
                email varchar(225),
                creation_source varchar(30),
                last_session_creation_time int, 
                opted_in_to_mailing_list int,
                enabled_for_marketing_drip int,
                org_id int,
                invited_by_user_id int,
                email_domain varchar(30)
            );"""
    conn = sqlite3.connect(ADOPT_DB)
    cursor = conn.cursor()
    cursor.execute(sql_create)
    conn.commit()
    conn.close()

        
def main():
    a = Analyzer()
    a.analyze_source()
    print()
    a.analyze_mailing_in_adopted()
    a.analyze_marketing_in_adopted()
    a.analyze_invited_in_adopted()
    a.analyze_isolated_in_adopted()
    a.analyze_org_in_adopted()
    print()
    a.analyze_invite_transfer()
    a.analyze_mailing_transfer()
    a.analyze_marketing_transfer()
    a.analyze_combine_transfer()
    a.analyze_org_transfer()
    a.analyze_org_combine_transfer()
    print()
    a.analyze_email_adopted()
    print()
    a.analyze_email_signin()
    
if __name__ == "__main__":
    main()   