# ~ ------------------------ [ Importing libraries ] ------------------------ ~
from flask import *
# ~ ------------------------ [ Declaring App ] ------------------------ ~
app = Flask(__name__)
''' ~ ------------------------ [ Defining useful dictionaries for html functionalities ] ------------------------ ~ '''
homepage = {
    'PageTitle' : "Página de Inicio",
    'user' : "Usuario",
    'password' : "Contraseña"
}

''' ~ ------------------------ [ Web Page Initializing ] ------------------------ ~ '''

@app.route('/') # starting the web page
def root():
    return render_template("login.html", homepage=homepage)

@app.route('/home')  # /home: page after login in
def home_page():
    return render_template("home_page.html")

if __name__ == "__main__": # keep debug = true so webpage keeps running
    app.run(debug=True)
    