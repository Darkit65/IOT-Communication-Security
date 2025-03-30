# Encryption code in Python using the `cryptography` library
from cryptography.fernet import Fernet

# Generate a key (this should be securely shared or stored for decryption)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt data
def encrypt_data(data):
    byte_data = data.encode()
    encrypted_data = cipher_suite.encrypt(byte_data)
    return encrypted_data

# Decrypt data
def decrypt_data(encrypted_data):
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data.decode()

# Example usage
data = "Sensitive IoT Data"
encrypted_data = encrypt_data(data)
print("Encrypted Data:", encrypted_data)
print("Decrypted Data:", decrypt_data(encrypted_data))
