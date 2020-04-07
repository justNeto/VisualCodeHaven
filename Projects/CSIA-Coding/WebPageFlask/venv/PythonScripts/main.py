from flask import Flask, render_template, request, url_for


app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html', title='Application', data = {'v1': 0, 'v2': 1, 'v3': 2})

@app.route('/homepage', methods=['POST'])
def dijs():
    destination = request.form['destination']
    origin = request.form['origin']
    return render_template('tryout.html', o=origin, d=destination)


if __name__ == '__main__':
    app.run(debug=True)
