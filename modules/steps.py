import modules.parsing as p
import modules.classes as c
from modules.app_state import AppState
import modules.io as io
def init(app: AppState):
    print("Please enter the password")
    check_password(input(), app)

def check_password(string, app: AppState):
    if string == app.app_password:
        present_options(app)
    else:
        print("Incorrect password")
        init(app)

def present_options(app: AppState):
    print("Type in a letter to select an option:\n"
          + "\t(L)ist all saved passwords\n"
          + "\t(A)dd a password\n"
          + "\t(U)pdate a password\n"
          + "\t(D)elete a password\n"
          + "\t(C)ommit changes\n"
          )
    options(input(), app)

def complete_step(string, app: AppState):
    print(string + "\n")
    present_options(app)

def list_pw(app: AppState):
    if len(app.uup_list) > 0:
        p.print_uup_list(app.uup_list)
        complete_step("Passwords retrieved successfully.", app)
    else: complete_step("No passwords are currently saved", app)

def add_pw(app: AppState):
    print("Enter the URL: ")
    url = input()
    already_in_list: bool = len(list(filter(lambda uup: uup.url.upper() == url.upper(), app.uup_list))) >= 1
    if not already_in_list:
        print("Enter the username: ")
        username = input()
        print("Enter the password: ")
        password = input()
        app.uup_list.append(c.UrlUserPass(url, username, password))
        complete_step("Password has been added.", app)
    else: complete_step("URL is already in the list.", app)

def update_pw(app: AppState):
    print("Enter the URL of the password to be updated: ")
    url = input()
    already_in_list: bool = len(list(filter(lambda uup: uup.url.upper() == url.upper(), app.uup_list))) >= 1
    if already_in_list:
        print("Enter the updated username: ")
        username = input()
        print("Enter the updated password: ")
        password = input()
        app.uup_list = list(filter(lambda uup: uup.url.upper() != url.upper(), app.uup_list))
        app.uup_list.append(c.UrlUserPass(url, username, password))
        complete_step("Password has been updated.", app)
    else: complete_step("URL not in the list.", app)

def delete_pw(app: AppState):
    print("Enter the URL of the password to be deleted: ")
    url= input()
    new_uup_list = list(filter(lambda uup: uup.url.upper() != url.upper(), app.uup_list))
    if len(app.uup_list) > len(new_uup_list):
        app.uup_list = new_uup_list
        complete_step("Password has been deleted.", app)
    else: complete_step("URL not in the list.", app)

def commit_pw(app: AppState):
    io.save_file(app.pw_filename, app.uup_list, app.app_password)
    #io.save_encrypted_file(app.pw_filename, app.uup_list, app.app_password)
    complete_step("Changes have been committed.", app)

def options(string, app: AppState):
    string = string.upper()
    if string == "L":
        list_pw(app)
        return
    if string == "A":
        add_pw(app)
        return
    if string == "U":
        update_pw(app)
        return
    if string == "D":
        delete_pw(app)
        return
    if string == "C":
        commit_pw(app)
        return
    print(string + " is not an option")
