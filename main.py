import random
from app.system import LoginSystem
from app.database_manager import DatabaseManager
from flask import Flask, render_template, request
from flask import session


app = Flask(__name__)

sys = LoginSystem()
app.secret_key = "your's key"

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username').lower()
        pw = request.form.get('password')
        return sys.login(user, pw)
    return render_template('login.html')
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_answer = request.form.get('user_answer')
        if int(user_answer) != session.get('captcha_result'):
            return "Jawaban Salah atau Captcha Kadaluarsa"
        user = request.form.get('username').lower()
        email = request.form.get('email').lower()
        password = request.form.get('password')
        return sys.register(user, email, password)
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    session['captcha_result'] = num1 + num2
    return render_template('register.html', n1=num1, n2=num2)

    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

    