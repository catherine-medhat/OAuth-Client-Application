from flask import Flask, jsonify, redirect, render_template, request
import secrets
import string

app = Flask(__name__,  static_folder='static')

stored_authorization_codes = {}

stored_access_tokens = {}

@app.route('/authorize', methods=['GET'])
def authorize():
    """
    Handles the authorization request from the client.
    Expects the client_id as a query parameter.
    If the client_id matches the expected value, renders the consent page.
    Otherwise, returns an error response.

    Returns:
        Consent page or error response in JSON format.
    """
    client_id = request.args.get('client_id')

    if client_id == 'the_client_id':
        return render_template('consent.html', client_id=client_id) 
    else:
        return jsonify({'error': 'Invalid client'}), 401

@app.route('/callback', methods=['POST'])
def callback():
    """
    Handles the callback request after the user approves the consent.

    Expects the client_id in the form data.
    Generates an authorization code and stores it for the client_id.

    Returns:
        HTML template with the authorization code.
    """
    client_id = request.form.get('client_id')
    authorization_code = generate_authorization_code() 
    stored_authorization_codes[client_id] = authorization_code

    return render_template('auth.html', authorization_code=authorization_code)

@app.route('/token', methods=['POST'])
def exchange_token():
    """
    Handles the token exchange request from the client.

    Expects the authorization code, client_id, and client_secret in the form data.
    Verifies the client credentials and the authorization code.
    If valid, generates an access token and returns it along with token type and expiration.

    Returns:
        Access token, token type, and expiration in JSON format.
    """
    authorization_code = request.form.get('code')
    client_id = request.form.get('client_id')
    client_secret = request.form.get('client_secret')

    if client_id != "the_client_id" or client_secret != 'the_client_secret':
        return jsonify({'error': 'Invalid client credentials'}), 401

    stored_auth_code = stored_authorization_codes.get(client_id)
    if stored_auth_code != authorization_code:
        return jsonify({'error': 'Invalid authorization code'}), 400

    access_token = generate_access_token()
    token_type = 'bearer'
    expires_in = 3600

    stored_access_tokens[access_token] = {
        'client_id': client_id,
        'expires_in': expires_in
    }

    return jsonify({'access_token': access_token, 'token_type': token_type, 'expires_in': expires_in})

def generate_authorization_code(length=16):
    """
    Generates a random authorization code.

    Arguments:
        length (int): Length of the authorization code.

    Returns:
        str: Authorization code.
    """
    characters = string.ascii_letters + string.digits
    code = ''.join(secrets.choice(characters) for _ in range(length))

    return code

def generate_access_token(length=16):
    """
    Generates a random access token.

    Arguments:
        length (int): Length of the access token.

    Returns:
        str: Access token.
    """
    characters = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(characters) for _ in range(length))

    return token

@app.route('/validate_token', methods=['POST'])
def validate_token():
    """
    Validates the access token sent by the client.

    Expects the access token in the JSON payload.
    Checks if the access token exists in the stored access tokens.

    Returns:
        Status of token validity in JSON format.
    """
    access_token = request.json.get('access_token')

    if access_token in stored_access_tokens:
        return jsonify({'status': 'valid'}), 200
    else:
        return jsonify({'status': 'invalid'}), 401

if __name__ == '__main__':
    app.run(port=8000)
