import boto3
import getpass
import json
import utils

def main():
    
    user = utils.get_user()
    user["clientid"] = utils.get_config()["clientid"]

    response = login(user)
    utils.save_tokens(response)

    refresh = refresh_token(
        utils.get_refresh_token(),
        utils.get_config()["clientid"]
    )
    utils.save_tokens(refresh)


def login(user:dict):
    ### Login with user={username:str, password:str, clientid:str} ###
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

def refresh_token(refeshToken:str, clientid:str):
    ### Refresh tokens with refreshToken.json ###
    client = boto3.client('cognito-idp', region_name='us-west-2')
    response = client.initiate_auth(
        AuthFlow='REFRESH_TOKEN_AUTH',
        AuthParameters={
            'REFRESH_TOKEN': refeshToken
        },
        ClientId=clientid
    )
    return response

if __name__ == "__main__":
    main()