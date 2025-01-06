import modules.parsing as p
import modules.encryption as e

def load_file(pw_filename, password):
    with open(pw_filename) as pwf:
        print("loading this file: " + pw_filename)
        #can only do this once PW has been validated
        file_contents = e.decode(pwf.read(), password)
        #if len(file_contents) > 0:
        return p.json_to_uup_list(file_contents)

def save_file(pw_filename, uup_list, password):
    with open(pw_filename, "w") as s:
        #s.write(p.uup_list_to_json(uup_list))
        s.write(e.encode(p.uup_list_to_json(uup_list), password))
