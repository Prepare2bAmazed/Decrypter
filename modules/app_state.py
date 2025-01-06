import modules.io as io

class AppState:
    def __init__(self, pw_filename):
        self.pw_filename = pw_filename
        self.app_password = ""
        self.uup_list = []
        self.encrypted_file_contents = io.load_file_basic(pw_filename)
