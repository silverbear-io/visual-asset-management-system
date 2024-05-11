import boto3
import getpass
import json

def main():
    
    user = get_user()
    config = load_config()
    user["clientid"] = config["clientid"]
    response = login(user)
    save_tokens(response)

    
    
def login(user:dict):
    print(f'logging in with u:{user["username"]}')
    client = boto3.client('cognito-idp',region_name='us-west-2')
    response = client.initiate_auth(
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            'USERNAME': user["username"],
            'PASSWORD': user["password"]
        },
        ClientId=user["clientid"]
    )
    return response

def save_tokens(response:dict):
    with open('accessToken.json', 'w') as f:
        f.write(response['AuthenticationResult']['AccessToken'])
    with open('refreshToken.json', 'w') as f:
        f.write(response['AuthenticationResult']['RefreshToken'])
    with open('idToken.json', 'w') as f:
        f.write(response['AuthenticationResult']['IdToken'])
    print(f"tokens saved")

def get_user():
    username = str(input("Username: "))
    password = getpass.getpass()
    return {"username": username, "password": password}

# Config file format:
# {
#   "clientid": "cognito webclient id"
# }
def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    main()