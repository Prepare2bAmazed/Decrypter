import cryptocode

def encode(message, password):
    return cryptocode.encrypt(message, password)

def decode(encoded, password):
    return cryptocode.decrypt(encoded, password)

#
# encoded = cryptocode.encrypt("mystring","mypassword")
#
# decoded = cryptocode.decrypt(encoded, "mypassword")


# def encrypt(message: bytes, key: bytes) -> bytes:
#     return Fernet(key).encrypt(message)
#
# def decrypt(token: bytes, key: bytes) -> bytes:
#     return Fernet(key).decrypt(token)

# def encrypt_string(password, string):
#     """Encrypts a string with a password using Fernet."""
#
#     # Generate a key from the password
#     key = Fernet.generate_key_from_password(password.encode(), b'salt')
#     fernet = Fernet(key)
#
#     # Encrypt the string
#     encrypted_string = fernet.encrypt(string.encode())
#     return encrypted_string
#
# def decrypt_string(password, encrypted_string):
#     """Decrypts a string with a password using Fernet."""
#
#     # Generate the same key from the password
#     key = Fernet.generate_key_from_password(password.encode(), b'salt')
#     fernet = Fernet(key)
#
#     # Decrypt the string
#     decrypted_string = fernet.decrypt(encrypted_string).decode()
#     return decrypted_string
#
# # Example usage
# password = "mysecretpassword"
# string_to_encrypt = "Hello, world!"
#
# encrypted_string = encrypt_string(password, string_to_encrypt)
# print("Encrypted string:", encrypted_string)
#
# decrypted_string = decrypt_string(password, encrypted_string)
# print("Decrypted string:", decrypted_string)

# key = Fernet.generate_key() #this is your "password"
# cipher_suite = Fernet(key)
# encoded_text = cipher_suite.encrypt(b"Hello stackoverflow!")
# decoded_text = cipher_suite.decrypt(encoded_text)

# def derive_key(password: str, salt: bytes) -> bytes:
#     kdf = PBKDF2HMAC(
#         algorithm=hashes.SHA256(),
#         length=32,
#         salt=salt,
#         iterations=100000,
#     )
#     temp = kdf.derive(password.encode())
#     print(temp)
#     return temp
#
# def encrypt_message(message: str, password: str) -> bytes:
#     salt = Fernet.generate_key()
#     key = derive_key(password, salt)
#     f = Fernet(key)
#     encrypted_message = f.encrypt(message.encode())
#     return salt + encrypted_message
#
# def decrypt_message(encrypted_message: bytes, password: str) -> str:
#     salt = encrypted_message[:32]
#     encrypted_message = encrypted_message[32:]
#     key = derive_key(password, salt)
#     f = Fernet(key)
#     decrypted_message = f.decrypt(encrypted_message)
#     return decrypted_message.decode()

# # Example usage:
# password = "mysecretpassword"
# message = "This is a secret message."
#
# encrypted_message = encrypt_message(message, password)
# print("Encrypted:", encrypted_message)
#
# decrypted_message = decrypt_message(encrypted_message, password)
# print("Decrypted:", decrypted_message)