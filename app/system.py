from app.database_manager import DatabaseManager
import hashlib
import os


class UserAccount:
    """class khusus untuk menangani akun pengguna"""
    def __init__(self, username, password):
        self.username = username
        self._password = password
        #Encapsulation.
    
    def _hash_password(self, password, salt=None):
        if salt is None:
            salt = "HeI_AnTeK_AnTeK_AsIng"
            #masih static Salt soalnya nggak mau ribet
            salted = salt + password
        return hashlib.sha256(salted.encode()).hexdigest()#kita gunakan sha256 standar industri sekarang
        
    def validate_email(self, email):
        if "@" in email and "." in email:
            return True
        return False
        
class LoginSystem(UserAccount):
    """class untuk Register/login pengguna"""
    def __init__(self):
        self.db = DatabaseManager()

    def register(self, usr, email, pw):
        if not self.validate_email(email):
            return f"Error {email} tidak valid"
        hashed_pw = self._hash_password(pw)
        if self.db.save_user(usr, email, hashed_pw):
            return f"Username {usr} Telah Di Daftarkan ke Database"
        return f"Error mungkin {usr} Sudah ada"
                
                
    def login(self, usr, pw):
        hashed_pw = self._hash_password(pw)
        query = "SELECT password FROM users WHERE username = ?"
        self.db.cursor.execute(query, (usr,))
        data = self.db.cursor.fetchone()#mengambil data dari database 
        if data:
            stored_pw = data[0]
            if stored_pw == hashed_pw:
                return f"[*] Selamat datang {usr}"
            else:
                return "[!]Password salah."
        else:
            return "[!]Username tidak terdaftar."

                
if __name__ == "__main__":
    pass