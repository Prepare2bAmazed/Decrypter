import json
import modules.classes as c

def json_to_uup_list(json_string):
    parsed_json = json.loads(json_string)
    domain_user_pass_list = []
    for j in parsed_json:
        domain_user_pass = c.UrlUserPass(j["url"], j["username"], j["password"])
        domain_user_pass_list.append(domain_user_pass)
    return domain_user_pass_list

def uup_list_to_json(uup_list):
    return json.dumps(uup_list, default=lambda o: o.__dict__)

dividing_line = "-" * 50

def print_uup_list(uup_list):
    print(dividing_line)
    sorted_list = sorted(uup_list, key=lambda UrlUserPass: UrlUserPass.url )
    for uup in sorted_list:
        print("URL: " + uup.url)
        print("Username: " + uup.username)
        print("Password: " + uup.password)
        print(dividing_line)