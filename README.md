
# OAuth2 Resource Server Example

This project demonstrates a simple implementation of an OAuth2 resource server using Flask in Python.

The project consists of three components:
- Resource Server: A Flask application that provides protected resources.
- OAuth Server: A Flask application that acts as the authorization server for issuing access tokens.
- Client: A Python script that demonstrates the OAuth2 authorization flow and accesses protected resources.

## Prerequisites

Before running the project, ensure that you have the following installed:
- Python 3.x
- Flask (`pip install flask`)
- Requests (`pip install requests`)

## Usage

1. Start the Resource Server:
   - Open a terminal or command prompt and navigate to the directory containing the resource server code.
   - Run the following command:
     ```
     python resource_server.py
     ```
   - The resource server will start running on `http://localhost:5000`.

2. Start the OAuth Server:
   - Open a new terminal or command prompt and navigate to the directory containing the OAuth server code.
   - Run the following command:
     ```
     python oauth_server.py
     ```
   - The OAuth server will start running on `http://localhost:8000`.

3. Run the Client:
   - Open a new Python script or a Python IDE.
   - Copy and paste the client code into the script or IDE.
   - Customize the client ID, client secret, redirect URI, authorization endpoint, and token endpoint variables in the script.
   - Save the script with a `.py` extension.
   - Run the script using the Python interpreter:
     ```
     python your_script_name.py
     ```
   - Follow the prompts in the script:
     - Visit the provided URL in a web browser for verification.
     - Confirm the consent on the consent page.
     - Copy the authorization code from the consent page and paste it into the script.
   - If successful, the script will print the access token and the protected resources retrieved from the resource server.

Make sure all three servers (resource server, OAuth server, and client) are running simultaneously in separate terminal or command prompt windows.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify and adapt the code according to your needs.

## Acknowledgments

This project was inspired by the Flask framework and the OAuth2 protocol.

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [OAuth 2.0 RFC](https://tools.ietf.org/html/rfc6749)

Please refer to the resources above for more information on Flask, OAuth2, and related topics.
