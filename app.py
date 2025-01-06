import modules.steps as s
from modules import app_state as a

app_state = a.AppState("text_files/passwords.txt")

s.init(app_state)