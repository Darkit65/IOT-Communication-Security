import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests
import datetime
import jwt
from cryptography.fernet import Fernet
from key_manager import load_key, generate_key

# Generate key if not already present
generate_key()
key = load_key()
cipher_suite = Fernet(key)

# Data to encrypt
data = "Sensitive information that needs to be encrypted"
print("Original Data:", data)

# Encrypt the data
encrypted_data = cipher_suite.encrypt(data.encode()).decode()
print("Encrypted Data:", encrypted_data)

# Prepare the JWT token
payload = {
    "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=30),
    "sub": "client_user"
}
jwt_token = jwt.encode(payload, 'your-secret-key', algorithm='HS256')
print("Encrypted JWT:", jwt_token)

# Headers with JWT token
headers = {
    'Authorization': f'Bearer {jwt_token}'
}

# Data payload
json_data = {
    "data": encrypted_data
}

# Send encrypted data
url = "https://127.0.0.1:5000/send-data"
response = requests.post(url, json=json_data, headers=headers, verify=False)

# Handle response
if response.status_code == 200:
    print("\nSuccessfully received response from server:")
    print("Server Response:", response.json())
else:
    print("\nError encountered:")
    print("Status Code:", response.status_code)
    print("Error Details:", response.json())
