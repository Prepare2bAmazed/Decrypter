import modules.steps as s
from modules import app_state as a

app_state = a.AppState("text_files/passwords.txt", "text_files/starting_data.json", "eggs")

s.init()
s.check_password(input(), app_state)