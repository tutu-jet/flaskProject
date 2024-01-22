from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 模拟用户数据库
users = [
    {'username': 'admin', 'password': 'admin'},
    {'username': 'user1', 'password': 'password1'},
    {'username': 'user2', 'password': 'password2'}
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        for user in users:
            if user['username'] == username and user['password'] == password:
                return redirect(url_for('dashboard'))

        error = 'Invalid username or password. Please try again.'
        return render_template('login.html', error=error)

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run()
