import uuid

class ReplayProtection:

    def __init__(self):
        self.used_nonces = []

    def generate_nonce(self):
        return str(uuid.uuid4())

    def verify_nonce(self, nonce):
        if nonce in self.used_nonces:
            return False
        self.used_nonces.append(nonce)
        return True