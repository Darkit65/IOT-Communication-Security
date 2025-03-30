import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests
import datetime
import jwt
from cryptography.fernet import Fernet

# Load the server's generated key (assuming the client also has access to it for testing)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt data
data = "Sensitive information that needs to be encrypted"
encrypted_data = cipher_suite.encrypt(data.encode()).decode()

# Set an invalid JWT token (manually tamper the token for testing)
payload = {
    "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=30),
    "sub": "client_user"
}
jwt_token = jwt.encode(payload, 'your-secret-key', algorithm='HS256')
jwt_token = jwt_token[:-3] + "xyz"  # Tamper with the token

# Prepare headers and data
headers = {
    'Authorization': f'Bearer {jwt_token}'
}
json_data = {
    "data": encrypted_data
}

# Send the data to the server
url = "https://127.0.0.1:5000/send-data"
response = requests.post(url, json=json_data, headers=headers, verify=False)

# Handle the server response
print("Server Response:", response.json())
