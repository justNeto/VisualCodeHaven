m_list = ["a01654419@itesm.mx", "a01654106@itesm.mx", "a01654202@itesm.mx"]  #  mails of all the members in the school
n_dict = {
    "a01654419@itesm.mx": 'Password1',
    "a01654202@itesm.mx": 'Password3',
    "a01654106@itesm.mx": 'Password1'
}
# dictionary of all the already existing accounts with usernames and passwords

id_mail = {"a01654106@itesm.mx": 'Password1'}


def create_user(m_list, n_dict, id_mail):
    for key in n_dict:
        if list(id_mail.keys())[0] == key:
            print(list(id_mail.keys())[0])
            return("This mail is already registered!")
            break
    for i in range(len(m_list)):
        if  m_list[i] == list(id_mail.keys())[0]:
            print(m_list[i])
            n_dict.update(id_mail)
            return n_dict
            print("It has now updated!")

print(create_user(m_list, n_dict, id_mail))
