import boto3
import getpass
import json

def get_access_token():
    with open('accessToken.json', 'r') as f:
        accessToken = f.read()
    return accessToken

def get_id_token():
    with open('idToken.json', 'r') as f:
        idToken = f.read()
    return idToken

def get_refresh_token():
    with open('refreshToken.json', 'r') as f:
        refreshToken = f.read()
    return refreshToken

def get_config():
    with open('config.json', 'r') as f:
        return json.load(f)

# Config file format:
# {
#   "clientid": "cognito webclient id"
#   "apig": "api gateway url"
# }
def get_user():
    username = str(input("Username: "))
    password = getpass.getpass()
    return {"username": username, "password": password}

def save_tokens(response:dict):
    with open('accessToken.json', 'w') as f:
        f.write(response['AuthenticationResult']['AccessToken'])
    with open('idToken.json', 'w') as f:
        f.write(response['AuthenticationResult']['IdToken'])
    
    # does not exist in response for init_auth:REFRESH_TOKEN_AUTH
    if 'RefreshToken' in response['AuthenticationResult']:
        with open('refreshToken.json', 'w') as f:
            f.write(response['AuthenticationResult']['RefreshToken'])
    
    print(f"tokens saved")