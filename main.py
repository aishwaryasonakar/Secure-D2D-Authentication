from device import Device
from authentication import Authentication
from challenge import Challenge
from replay_protection import ReplayProtection
from logger import Logger
from ecc import ECC
from ecdh import ECDH
from aes import AES128

# Create devices
device_a = Device("Device A")
device_b = Device("Device B")

# ECC Key Generation
ecc_a = ECC()
ecc_b = ECC()

# Exchange Public Keys
public_key_a = ecc_a.get_public_key()
public_key_b = ecc_b.get_public_key()

# Load Public Keys
peer_key_a = ecc_a.load_public_key(public_key_b)
peer_key_b = ecc_b.load_public_key(public_key_a)

# Generate Shared Secret
ecdh = ECDH()

shared_key_a = ecdh.generate_shared_secret(
    ecc_a.private_key,
    peer_key_a
)

shared_key_b = ecdh.generate_shared_secret(
    ecc_b.private_key,
    peer_key_b
)
print("\n========== ECC ==========")
print("ECC Public Key A Generated")
print("ECC Public Key B Generated")

print("\n========== ECDH ==========")
print("Shared Secret Generated Successfully")
print("Shared Key Length:", len(shared_key_a))

# Create objects
auth = Authentication()
challenge = Challenge()
replay = ReplayProtection()
logger = Logger()

# Connect devices
device_a.connect()
device_b.connect()

# Authentication
key = input("Enter Secret Key: ")

if auth.authenticate(key):

    print("\nAuthentication Successful")
    logger.log("Authentication Successful")

    # Challenge Response
    random_number = challenge.generate()
    print("\nChallenge Number:", random_number)

    answer = int(input("Enter Challenge Number Again: "))

    if challenge.verify(random_number, answer):

        print("\nChallenge Verified")
        logger.log("Challenge Verified")

        # Replay Protection
        nonce = replay.generate_nonce()
        print("Generated Nonce:", nonce)

        if replay.verify_nonce(nonce):

            print("Nonce Verified")
            logger.log("Nonce Verified")

            # AES-128 using ECDH Shared Secret
            aes_a = AES128(shared_key_a)
            aes_b = AES128(shared_key_b)

            message = "Hello Device B"

            encrypted = aes_a.encrypt(message)

            print("\nEncrypted Message:", encrypted)

            decrypted = aes_b.decrypt(encrypted)

            print("Decrypted Message:", decrypted)

            logger.log("Encrypted Communication Successful")

        else:

            print("\nReplay Attack Detected")
            logger.log("Replay Attack Detected")

    else:

        print("\nChallenge Verification Failed")
        logger.log("Challenge Verification Failed")

else:

    print("\nAuthentication Failed")
    logger.log("Authentication Failed")