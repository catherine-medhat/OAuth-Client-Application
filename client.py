import requests

def get_authorization_code():
    """
    Prompt the user to enter the authorization code.

    Returns:
    str: The authorization code entered by the user.
    """
    authorization_code = input("Enter the authorization code: ")
    return authorization_code


def send_token_request(client_id, client_secret, redirect_uri, authorization_code):
    """
    Send a token request to the token endpoint.

    Arguments:
    client_id (str): The client ID.
    client_secret (str): The client secret.
    redirect_uri (str): The redirect URI.
    authorization_code (str): The authorization code.

    Returns:
    dict: The token response data.
    """
    token_endpoint = 'http://localhost:8000/token'
    token_params = {
        'code': authorization_code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri
    }
    response = requests.post(token_endpoint, data=token_params)
    return response.json()


def access_resource_server(access_token):
    """
    Access the resource server using the provided access token.

    Arguments:
    access_token (str): The access token.

    Returns:
    dict: The resource server response.
    """
    resource_server_url = 'http://localhost:5000/resource'
    headers = {'Authorization': 'Bearer ' + access_token}
    resource_response = requests.get(resource_server_url, headers=headers)
    return resource_response.json()


def main():
    """
    Perform the main flow of the client application.

    This function prompts the user for authorization code, sends a token request to the token endpoint,
    and accesses the resource server using the obtained access token.
    """
    client_id = 'the_client_id'
    client_secret = 'the_client_secret'
    redirect_uri = 'http://localhost:8000/callback'
    authorization_endpoint = 'http://localhost:8000/authorize'

    authorization_url = authorization_endpoint + '?client_id=' + client_id
    print("Please visit the following URL and verify:")
    print(authorization_url)

    authorization_code = get_authorization_code()

    token_data = send_token_request(client_id, client_secret, redirect_uri, authorization_code)

    if 'access_token' in token_data:
        access_token = token_data['access_token']
        print("Access token:", access_token)
        resource_data = access_resource_server(access_token)
        print("Resources:")
        print(resource_data)
    else:
        print("Error: No access token was found in token response")


if __name__ == '__main__':
    main()
