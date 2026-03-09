import sqlite3

class DatabaseManager:
    def __init__(self, db_name = ".protected.db"):
        self.database = db_name
        self.conn = sqlite3.connect(self.database)
        self.cursor = self.conn.cursor()
        self.db_init()
        
    def execute_query(self, query, params=()):
        try:
            with self.conn:
                self.cursor.execute(query, params)
        except sqlite3.Error as e:
            print(f"[E] Error: {e}")
        
    
    def db_init(self):
        query = """
        CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
        email TEXT UNIQUE)"""
        try:
            self.execute_query(query)
            return True
        except sqlite3.OperationalError:
            return False 
    
    def save_user(self, usr, pw, email):
        query = """INSERT INTO users(username, password, email) VALUES (?, ?, ?)"""
        self.execute_query(query, (usr, pw, email))
        print("Berhasil menambahkan")
        
if __name__ == "__main__":
    pass
