import modules.parsing as p

def init_pw_list(pw_filename):
    with open(pw_filename) as pwf:
        return p.json_to_uup_list(pwf.read())

class AppState:
    def __init__(self, pw_filename, starting_filename, app_password):
        self.pw_filename = pw_filename
        self.starting_filename = starting_filename
        self.app_password = app_password
        self.uup_list = init_pw_list(pw_filename)
