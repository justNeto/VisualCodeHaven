from flask import Flask, render_template

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login/homepage')
def homepage():
    return render_template('homepage.html', title='Application')
