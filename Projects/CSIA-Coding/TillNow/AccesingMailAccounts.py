"""

Author: ZXxNetoxXZ
Tentative program to login or register new members of the campus into the web page.

"""

m_list = ["a01654419@itesm.mx", "a01654106@itesm.mx", "a01654202@itesm.mx"]  #  list of all mails in the school by my client
mp_dict = { # usernames(mails) and passwords for registered accounts
    "a01654419@itesm.mx": "Password1",
    "a01654202@itesm.mx": "Password3",
    }

def login_toPage():
    emp_dict = dict() #entered mail and password dict
    # Both username and password should be associated with a GUI element
    username = input()
    password = input()
    emp_dict[username] = password
    if username in mp_dict.keys() and password == mp_dict.get(username):
        print("Login in...")
        # Access the next page
    else:
        print("The username or password is wrong! Try again!")


def register():
    # Again, associate both username to GUI elements
    emp_dict = dict()
    username = input()
    password = input()
    emp_dict[username] = password
    print(emp_dict)
    if username in mp_dict.keys() and username in m_list:
        print("The mail is already registered") # Checking for username in m_list is a layer of security
    elif username not in m_list:
        print("This mail does not exist! Be careful")
    else:
        mp_dict.update(emp_dict)
