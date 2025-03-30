import urllib3
import requests
import datetime  # Import datetime module
import jwt
from cryptography.fernet import Fernet
import time

# Disable HTTPS warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Load the server's generated key (assuming the client also has access to it for testing)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt data
data = "Sensitive information that needs to be encrypted"
encrypted_data = cipher_suite.encrypt(data.encode()).decode()

# Use a very short expiration time for the JWT token to test expiration
payload = {
    "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=1),  # 1-second expiration
    "sub": "client_user"
}
jwt_token = jwt.encode(payload, 'your-secret-key', algorithm='HS256')

# Prepare headers and data as usual
headers = {
    'Authorization': f'Bearer {jwt_token}'
}
json_data = {
    "data": encrypted_data
}

# Wait for the token to expire
time.sleep(2)  # Wait 2 seconds, so the token has expired

# Send the request
url = "https://127.0.0.1:5000/send-data"
response = requests.post(url, json=json_data, headers=headers, verify=False)

# Handle the server response
print("Server Response:", response.json())
