from app.system import LoginSystem
from app.database_manager import DatabaseManager
from flask import Flask, render_template, request

app = Flask(__name__)
sys = LoginSystem()
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    pw = request.form.get('password')
    result = sys.login(user, pw)
    