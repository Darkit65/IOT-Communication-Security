from cryptography.fernet import Fernet
import os

KEY_FILE = 'secret.key'

def generate_key():
    """
    Generate and save a new Fernet key if it doesn't already exist.
    """
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as key_file:
            key_file.write(key)
        print("New encryption key generated and saved.")
    else:
        print("Encryption key already exists.")

def load_key():
    """
    Load the existing Fernet key from the key file.
    """
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, 'rb') as key_file:
            key = key_file.read()
        return key
    else:
        raise FileNotFoundError("Encryption key not found. Run `generate_key()` to create it.")
