import cryptocode

def encode(message, password) -> str:
    return cryptocode.encrypt(message, password)

def decode(encoded, password) -> bool | str:
    return cryptocode.decrypt(encoded, password)
