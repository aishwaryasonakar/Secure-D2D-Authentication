from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

class AES128:

    def __init__(self, key):
        self.key = key[:16]

    def encrypt(self, plaintext):
        iv = os.urandom(16)

        cipher = Cipher(
            algorithms.AES(self.key),
            modes.CFB(iv)
        )

        encryptor = cipher.encryptor()

        ciphertext = encryptor.update(
            plaintext.encode()
        ) + encryptor.finalize()

        return iv + ciphertext

    def decrypt(self, encrypted_data):

        iv = encrypted_data[:16]
        ciphertext = encrypted_data[16:]

        cipher = Cipher(
            algorithms.AES(self.key),
            modes.CFB(iv)
        )

        decryptor = cipher.decryptor()

        plaintext = decryptor.update(
            ciphertext
        ) + decryptor.finalize()

        return plaintext.decode()