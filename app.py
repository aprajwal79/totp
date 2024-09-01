from flask import Flask, request, jsonify
import pyotp

app = Flask(__name__)

# Dictionary to store the secrets associated with emails (for demo purposes)
secrets = {
    "yourfriend@example.com": "U2EDRIKL2XL5M2IG",  # Example base32 secret
    "rushabhlute@outlook.com": "7C6R4FZYU33JI6MX"
}

def generate_totp(email):
    """Generate TOTP for the given email using the appropriate secret."""
    if email == "google":
        secret = "QVSGXI3YVSJBKFK3GB3XQBFNQI675N2G"
    elif email in secrets:
        secret = secrets[email]
    else:
        secret = "JBSWY3DPEHPK3PXP"  # Default secret

    totp = pyotp.TOTP(secret)
    return totp.now()

@app.route('/totp', methods=['GET'])
def totp_endpoint():
    email = request.args.get('email')
    if not email:
        return jsonify({"error": "Email parameter is missing"}), 400

    totp_code = generate_totp(email)
    if totp_code:
        #return jsonify({"email": email, "totp": totp_code})
        return totp_code
    else:
        return jsonify({"error": "Email not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
