from flask import Flask, jsonify, request
import requests
app = Flask(__name__)

@app.route('/resource', methods=['GET'])
def resource():
    """
    Handle the resource endpoint request.

    Returns:
    flask.Response: JSON response containing the resources or an error message.
    """
    access_token = request.headers.get('Authorization').split(' ')[1]

    if validate_access_token(access_token):
        return jsonify({'resources': ['Cathy', 'M']}), 200
    else:
        return jsonify({'error': 'Invalid token'}), 401

def validate_access_token(access_token):
    """
        Validate the access token by sending a request to the OAuth server.

        Arguments:
        access_token (str): The access token to validate.

        Returns:
        bool: True if the access token is valid, False otherwise.
        """
    oauth_server_url = 'http://localhost:8000/validate_token'
    response = requests.post(oauth_server_url, json={'access_token': access_token})

    if response.status_code == 200:
        return True
    else:
        return False

if __name__ == '__main__':
    app.run(port=5000)
