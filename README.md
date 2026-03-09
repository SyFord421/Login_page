# 🛡️ Simple Web Login System with Flask & SQLite

Sistem login dan registrasi sederhana yang dibangun menggunakan **Python (Flask)** sebagai backend, **SQLite** sebagai database, dan **HTML/CSS** untuk antarmuka pengguna. Project ini menggunakan konsep Pemrograman Berorientasi Objek (OOP) dan keamanan hashing password.

## ✨ Fitur Utama
* **Secure Hashing**: Password disimpan dalam bentuk hash SHA-256 dengan Static Salt.
* **Modular Architecture**: Pemisahan logika antara Database Manager, System Account, dan Web Interface.
* **Responsive UI**: Tampilan web yang bersih dan minimalis.
* **Database Persistence**: Data pengguna tersimpan aman dalam file `.protected.db`.

## 🛠️ Teknologi yang Digunakan
* **Python 3**
* **Flask** (Web Framework)
* **SQLite3** (Database)
* **HTML5 & CSS3**

## 📂 Struktur Folder
```text
.
├── app/
│   ├── database_manager.py  # Logic manajemen SQLite
│   └── system.py            # Logic Hashing & User Account
├── templates/
│   ├── login.html           # UI Halaman Login
│   └── register.html        # UI Halaman Register
├── main.py                  # Entry point CLI
└── main.py               # Entry point Web (Flask)
