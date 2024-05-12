import boto3
import requests
import json
import login
import utils


def main():
    config =utils.get_config()
    idToken = utils.get_id_token()
    dbs = get_databases(config['apig'], idToken)


def get_databases(apig:str, idToken:str):
    request = requests.get(f'{apig}/databases', headers={
        'Authorization': idToken
    })
    print(request.status_code)
    print(request.json())

if __name__ == "__main__":
    main()