import json
import requests
from snapp_email import ApiClient
from snapp_email.datacontract import classes
import examples.config as config
import examples.login as login
import examples.create_post as create_post


def get_chat_id_for_email_http(email_address, access_token):
    url = '{}/stream'.format(config.API_URL)

    data = {
        'User': {
            '$type': 'User_14',
            'AccountList': [{
                '$type': 'AccountEmail_14',
                'Email': email_address
            }]
        }
    }

    response = requests.post(
        url=url,
        headers={
            'Accept': 'application/vnd.4thoffice.stream.user-5.3+json',
            'Content-Type': 'application/vnd.4thoffice.stream.user-5.3+json',
            'Authorization': access_token
        },
        data=json.dumps(data)
    )

    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)

    card_chat_id = data['Id']

    return card_chat_id


def post_to_chat_http(chat_id, content, access_token):
    create_post.create_reply_http(chat_id, content, access_token)


def get_chat_id_for_email_sdk(email_address):
    api_client = ApiClient(username=config.INTEGRATION_KEY,
                           password=config.INTEGRATION_SECRET,
                           auth_type=7,
                           api_url=config.API_URL)

    user = create_post.create_user_object_from_email(email_address)
    stream_user = classes.StreamUser_22(User=user)

    response = api_client.stream.StreamUser_22.create(stream_user)
    return response.Id


def post_to_chat_sdk(chat_id, content):
    create_post.create_reply_sdk(chat_id, content)
