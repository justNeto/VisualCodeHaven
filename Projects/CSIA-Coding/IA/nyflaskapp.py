# ~ ------------------------ [ Importing libraries ] ------------------------ ~
from flask import Flask
# ~ ------------------------ [ Declaring App ] ------------------------ ~
app = Flask(__name__)

''' ~ ------------------------ [ Web Page Initializing ] ------------------------ ~ '''

@app.route('/') # starting the web page
def root():
    return render_template("index.html")

@app.route('/home')  # /home: page after login in
def home_page():
    return render_template("home_page.html")

if __name__ == "__main__": # keep debug = true so webpage keeps running
    app.run(debug=True)
    
