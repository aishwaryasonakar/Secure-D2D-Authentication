from cryptography.fernet import Fernet

class Encryption:

    def __init__(self, key=None):
        if key is None:
            self.key = Fernet.generate_key()
        else:
            self.key = key

        self.cipher = Fernet(self.key)

    def get_key(self):
        return self.key

    def encrypt(self, message):
        return self.cipher.encrypt(message.encode())

    def decrypt(self, encrypted_message):
        return self.cipher.decrypt(encrypted_message).decode()