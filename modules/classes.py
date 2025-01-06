import json
class UrlUserPass:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
    def  to_json (self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__)