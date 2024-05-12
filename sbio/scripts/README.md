# Testing APIs

1) Create a config.json 

    ```
    {
        "clientid": "cognito clientid",
        "apig": "api gateway url"
    }
    ```
2) Use `python login.py` with username and password in the CLI prompts to get tokens: accessToken.json, idToken.json, refreshToken.json.  **TODO**: convert these to actual tokens from raw string in file.

3) idToken is the JWT token used in API calls.  
    ```
    request = requests.get(
        f'{apig}/databases', 
        headers={'Authorization': idToken}
    )
    ```

**TODO**:
- update tokens.json to be valid json instead of just text strings in the file
- update agpig url to be api.vams.silverbear.io