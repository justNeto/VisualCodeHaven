from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html', title='Application')

if __name__ == '__main__':
    app.run(debug=True)
