import modules.parsing as p
import modules.classes as c
from modules.app_state import AppState
import modules.io as io

def init(app: AppState):
    welcome_options_menu(app)

def check_password(app: AppState):
    print("Type in the password")
    string = input()
    app.uup_list = p.encrypted_contents_to_list(app.encrypted_file_contents, string)
    if app.uup_list or app.app_password == string:
        app.app_password = string
        print("Password is correct.\n")
        app_options_menu(app)
    else:
        print("No content was unlocked with that password.")
        welcome_options_menu(app)

def new_password(app: AppState):
    print("Enter a new password for this app and delete all saved passwords. Close the app now to retain all saved passwords.")
    app.app_password = input()
    welcome_options_menu(app)

def welcome_options_menu(app: AppState):
    print("Type a letter to select an option:\n"
          +"\t(T)ype in the password for this app\n"
          + "\t(E)rase all saved passwords and set a new password for this app"
          )
    welcome_options(input(), app)

def welcome_options(string, app: AppState):
    string = string.upper()
    if string == "T":
        check_password(app)
        return
    if string == "E":
        new_password(app)
        return
    print(string + " is not an option")
    welcome_options_menu(app)

def app_options_menu(app: AppState):
    print("Type a letter to select an option:\n"
          + "\t(L)ist all saved passwords\n"
          + "\t(A)dd a password\n"
          + "\t(U)pdate a saved password\n"
          + "\t(D)elete a saved password\n"
          + "\t(C)ommit changes and save to file\n"
          + "\t(S)et a new password for this app\n"
          )
    app_options(input(), app)

def complete_step(string, app: AppState):
    print(string + "\n")
    app_options_menu(app)

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
    io.save_encrypted_file(app.pw_filename, app.uup_list, app.app_password)
    complete_step("Changes have been committed.", app)

def change_app_pw(app: AppState):
    print("Enter the the new password for this app: ")
    app.app_password = input()
    io.save_encrypted_file(app.pw_filename, app.uup_list, app.app_password)
    complete_step("Password has been changed.", app)

def app_options(string, app: AppState):
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
    if string == "S":
        change_app_pw(app)
        return
    print(string + " is not an option")
    app_options_menu(app)
