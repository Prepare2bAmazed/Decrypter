import modules.parsing as p
import modules.encryption as e

def load_file_basic(pw_filename) -> str:
    with open(pw_filename) as pwf:
        return pwf.read()

def save_encrypted_file(pw_filename, uup_list, password):
    with open(pw_filename, "w") as s:
        s.write(e.encode(p.uup_list_to_json(uup_list), password))
