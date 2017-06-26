import json
import requests
from snapp_email import ApiClient
import examples.config as config

access_token = None


def login():
    endpoint = '{0}/{1}'.format(config.API_URL, 'user/session/logon')

    response = requests.post(
        endpoint,
        headers={
            'Accept': 'application/vnd.4thoffice.logon.user-v4.0+json',
            'Content-Type': 'application/vnd.4thoffice.logon.user-v4.0+json'
        },
        data=json.dumps({
            "Authentication": {
                "AuthenticationType": 7,
                "AuthenticationId": config.INTEGRATION_KEY,
                "AuthenticationToken": config.INTEGRATION_SECRET
            },
            "ClientApplication": {
                "Type": 0,
                "Version": "0.1",
                "CodeName": "Bots"
            }
        })
    )

    if response.status_code != 200:
        response.raise_for_status()

    data = json.loads(response.text)
    return 'Bearer ' + data['Token']['AccessToken']


def login_http():
    global access_token
    if not access_token:
        print('Getting access token...')
        access_token = login()

    return access_token


def login_sdk():
    global access_token
    if not access_token:
        print('Getting access token...')
        api_client = ApiClient(username=config.INTEGRATION_KEY,
                               password=config.INTEGRATION_SECRET,
                               auth_type=7,
                               api_url=config.API_URL)
        access_token = api_client.get_access_token()

    return access_token
