from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return 'This is the root'

