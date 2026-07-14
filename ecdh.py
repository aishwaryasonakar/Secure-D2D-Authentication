from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
class ECDH:

    def generate_shared_secret(self, private_key, peer_public_key):
        shared_secret = private_key.exchange(
            ec.ECDH(),
            peer_public_key
        )

        return shared_secret