import unittest
import modules.encryption as e

class TestEncryption(unittest.TestCase):
    def test_encrypt_decrypt(self):
        message = "Here is the message"
        password = "ThisIsThePass"

        encrypted_message = e.encode(message, password)
        decrypted_message = e.decode(encrypted_message, password)
        decrypted_message_bad_pass = e.decode(encrypted_message, "ThiIsNotThePass")

        self.assertEqual(message, decrypted_message)
        self.assertEqual(False, decrypted_message_bad_pass)
