from app.database_manager import DatabaseManager
import bcrypt
import os
from typing import Final

class UserAccount:
    """class khusus untuk menangani akun pengguna"""
    def __init__(self):
        pass


    def _hash_password(self, password:str):
        """Melakukan Hashing pada password"""
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed.decode('utf-8')


    def validate_email(self, email:str) -> bool:
        """Memvalidasi Email Secara Sederhana"""
        if "@" in email and "." in email:
            return True
        return False



    def min_length(self, name:str, pw:str) -> bool:
        """memvalidasi agar input pengguna tidak terlalu pendek"""
        if len(name) < 5 or len(pw) < 5:
            return False
        return True


class LoginSystem(UserAccount):
    """Class Utama"""
    def __init__(self):
        self.db = DatabaseManager()#memulai inisiasi database


    def register(self, usr:str, email:str, pw:str):
        """Registrasi pengguna"""
        if not self.validate_email(email):
            return f"Error {email} tidak valid"
        if not self.min_length(usr, pw):
            return "Username atau password terlalu pendek minimal 5"
        hashed_pw = self._hash_password(pw)
        if self.db.save_user(usr, email, hashed_pw):
            return f"Username {usr} Telah Di Daftarkan ke Database"
        return f"Error mungkin {usr} Sudah ada"


    def login(self, usr:str, pw:str):
        query = "SELECT password FROM users WHERE username = ?"
        self.db.cursor.execute(query, (usr,))
        data = self.db.cursor.fetchone()#mengambil data dari database 
        if data:
            stored_pw = data[0]
            if bcrypt.checkpw(pw.encode('utf-8'), stored_pw.encode('utf-8')):
                return f"[*] Selamat datang {usr}"
            else:
                return "[!]Password salah."
        else:
            return "[!]Username tidak terdaftar."

                
if __name__ == "__main__":
    pass