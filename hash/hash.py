# import hashlib
# from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
# from cryptography.hazmat.backends import default_backend
# import os, base64


# def gen_key(bit: int) -> str:
#     aes_key = os.urandom(bit)
#     return base64.b64encode(aes_key).decode('utf-8')

# def create_device_key(data: str, secret_key: str) -> str:
#     # Combine the deviceID, principal, and SecretKey
#     combined = data + secret_key

#     # Generate the salt by hashing the combined string twice using MD5
#     salt = hashlib.sha256(hashlib.sha256(combined.encode()).hexdigest().encode()).hexdigest()

#     # Use this salt in further processing if needed
#     return salt

# device_token_cache = {}

# def get_or_create_device_token(data: str, secret_key: str) -> str:
#     if device_id in device_token_cache:
#         return device_token_cache[device_id]

#     device_key = create_device_key(data, secret_key)
#     device_token_cache[device_id] = device_key
#     return device_key


# def encrypt_device_token(device_token: str, key: bytes) -> bytes:
#     iv = os.urandom(16)
#     cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
#     encryptor = cipher.encryptor()
#     encrypted_device_token = iv + encryptor.update(device_token.encode()) + encryptor.finalize()
#     return encrypted_device_token

# def decrypt_device_token(encrypted_device_token: bytes, key: bytes) -> str:
#     iv = encrypted_device_token[:16]
#     cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
#     decryptor = cipher.decryptor()
#     decrypted_device_token = decryptor.update(encrypted_device_token[16:]) + decryptor.finalize()
#     return decrypted_device_token.decode()

# # Example usage
# key = os.urandom(32)  # AES-256 key
# device_id = "example_device_id"
# encrypted_device_token = encrypt_device_token(device_id, key)
# decrypted_device_token = decrypt_device_token(encrypted_device_token, key)

# device_token_returned = {}

# def authenticate_and_return_token(data: str, secret_key: str) -> str:
#     if device_token_returned.get(device_id, False):
#         return "DeviceToken already returned"

#     device_token = get_or_create_device_token(data, secret_key)
#     device_token_returned[device_id] = True
#     return device_token

# def reauthenticate_if_missing_token(device_id: str, token_received: bool):
#     if not token_received:
#         print("Token missing, re-authenticating from INITIAL")
#         # Initiate the authentication process again

