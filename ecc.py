from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

class ECC:

    def __init__(self):
        self.private_key = ec.generate_private_key(
            ec.SECP256R1()
        )

        self.public_key = self.private_key.public_key()

    def get_public_key(self):
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    def load_public_key(self, public_key_bytes):
        return serialization.load_pem_public_key(public_key_bytes)