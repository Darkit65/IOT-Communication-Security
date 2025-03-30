from cryptography.fernet import Fernet

# Generate the Fernet key
key = Fernet.generate_key()

# Print the key
print("Generated Fernet Key:", key.decode())
