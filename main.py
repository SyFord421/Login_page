from app.system import LoginSystem
from app.database_manager import DatabaseManager

from flask import Flask, render_template, request

app = Flask(__name__)
sys = LoginSystem()
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register_page')
def register_page():
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        pw = request.form.get('password')
        return sys.login(user, pw)
    return render_template('login.html')
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        return sys.register(user, email, password)
    return render_template('register.html')

    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

    