from cryptography.fernet import Fernet
from flask import Flask, request, jsonify
import jwt
from key_manager import load_key, generate_key

# Generate key if not already present
generate_key()
key = load_key()
cipher_suite = Fernet(key)

# JWT secret key (keep this safe)
JWT_SECRET_KEY = 'your-secret-key'

app = Flask(__name__)

@app.route('/send-data', methods=['POST'])
def receive_data():
    token = request.headers.get('Authorization').split()[1]
    
    # Validate JWT token
    try:
        jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401

    # Decrypt received data
    encrypted_data = request.json.get("data")
    try:
        decrypted_data = cipher_suite.decrypt(encrypted_data.encode()).decode()
        print("Decrypted Data:", decrypted_data)
        return jsonify({"status": "success", "message": "Data received and decrypted successfully"})
    except Exception as e:
        print("Decryption failed:", str(e))
        return jsonify({"status": "error", "message": "Decryption failed"}), 500

if __name__ == '__main__':
    app.run(ssl_context='adhoc')
