import modules.parsing as p
import modules.encryption as e

def load_file(pw_filename):
    with open(pw_filename) as pwf:
        file_contents = pwf.read()
        #if len(file_contents) > 0:
        return p.json_to_uup_list(file_contents)

def save_file(pw_filename, uup_list):
    with open(pw_filename, "w") as s:
        s.write(p.uup_list_to_json(uup_list))

def load_encrypted_file():
        return

def save_encrypted_file(pw_filename, uup_list, app_password):
    with open(pw_filename, "w") as s:
        s.write(e.encode(p.uup_list_to_json(uup_list), app_password))