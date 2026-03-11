import sqlite3

class DatabaseManager:
    def __init__(self, db_name = ".protected.db"):
        self.database = db_name
        self.conn = sqlite3.connect(self.database, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.db_init()
        
    def execute_query(self, query, params=()):
        try:
            with self.conn:
                self.cursor.execute(query, params)
        except sqlite3.Error as e:
            print (e)
    
    def db_init(self):
        query = """
        CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        email TEXT UNIQUE,
        password TEXT)"""
        try:
            self.execute_query(query)
            return True
        except sqlite3.OperationalError:
            return False 
    
    def save_user(self, usr, email, pw):
        query = """INSERT INTO users(username, email, password) VALUES (?, ?, ?)"""
        try:
            self.execute_query(query, (usr, email, pw))
            return True
        except Exception as e:
            return e
if __name__ == "__main__":
    pass
