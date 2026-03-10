from app.database_manager import DatabaseManager
import hashlib
import os


class UserAccount:
    """class khusus untuk menangani akun pengguna"""
    def _hash_password(self, password, salt=None):
        if salt is None:
            salt = "HeI_AnTeK_AnTeK_AsIng"
            #masih static Salt soalnya nggak mau ribet
            salted = salt + password
        return hashlib.sha256(salted.encode()).hexdigest()#kita gunakan sha256 standar industri sekarang
        
    def __init__(self, username, password):
        self.username = username
        self._password = password
        
        #Encapsulation.
        
class LoginSystem(UserAccount):
    """class untuk Register/login pengguna"""
    def __init__(self):
        self.db = DatabaseManager()

    def register(self, usr, pw, email):
        hashed_pw = self._hash_password(pw)
        if self.db.save_user(usr, hashed_pw):
            return f"Username {usr} Telah Di Daftarkan ke Database"
        else:
            return f"Gagal daftar, mungkin nama {usr} udah ada."
            
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