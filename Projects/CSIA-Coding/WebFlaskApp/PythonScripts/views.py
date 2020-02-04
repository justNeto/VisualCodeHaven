from PythonScripts import app
from flask import render_templates

@app.route('/')
def index():
    return render_templates('index.html')
