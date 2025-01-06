import json
import modules.classes as c
import modules.encryption as e

def json_to_uup_list(json_string) -> list | list[c.UrlUserPass]:
    parsed_json = []
    try:
        parsed_json = json.loads(json_string)
    except ValueError:
        return parsed_json

    url_user_pass_list = []
    for j in parsed_json:
        url_user_pass = c.UrlUserPass(j["url"], j["username"], j["password"])
        url_user_pass_list.append(url_user_pass)
    return url_user_pass_list

def uup_list_to_json(uup_list) -> str:
    return json.dumps(uup_list, default=lambda o: o.__dict__)

def print_uup_list(uup_list):
    dividing_line = "-" * 50
    print(dividing_line)
    sorted_list = sorted(uup_list, key=lambda uup: uup.url )
    for uup in sorted_list:
        print("URL: " + uup.url)
        print("Username: " + uup.username)
        print("Password: " + uup.password)
        print(dividing_line)

def encrypted_contents_to_list(encrypted_file_contents, password) -> list | list[c.UrlUserPass]:
    decoded = e.decode(encrypted_file_contents, password)
    if decoded:
        return json_to_uup_list(decoded)
    else:
        return []
