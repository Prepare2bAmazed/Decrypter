import modules.io as io

class AppState:
    def __init__(self, pw_filename, starting_filename, app_password):
        self.pw_filename = pw_filename
        self.starting_filename = starting_filename
        self.app_password = app_password
        self.uup_list = io.load_file(pw_filename, app_password)
