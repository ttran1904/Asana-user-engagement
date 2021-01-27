from User import User

# Find adopted-users and their specific time of adoption
class SignInUser(User):
    def __init__(self, db_path):
        user_conn = self.create_connection(db_path)
        self.users = self.filter_signed_in_user(user_conn)
        
        self.users = self.tuple_to_list(self.users)

    # Only look at users who actually signed into Asana >= 1 time.
    # Look at the User data.
    def filter_signed_in_user(self, connection):
        query = "SELECT object_id FROM User WHERE last_session_creation_time != '' "
        posts = self.execute_read_query(connection, query)
        return posts
    
    # Convert from list of tuples to just list of signed in users.
    def tuple_to_list(self, list_tuples):
        l = []
        for t in list_tuples:
            l.append(t[0])
        return l

