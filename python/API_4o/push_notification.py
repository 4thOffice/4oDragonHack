import json

import requests
import python.smart_assistant_example.config as config
from python.API_4o.authorization import access_token


def send_push_notification(user_id, custom_id, push_notification_message):
    data = {
            'Recipient': {
                'Id': user_id
            },
            'Sender': {
                'Id': ''
            },
            'ActionMessage': push_notification_message,
            'TriggerList': [{
                'NotificationTriggerType': 'ActionListUpdated',
                'ResourceId': custom_id
            }]
        }

    url = '{}/notification'.format(config.API_4O['URL'])

    response = requests.post(
        url=url,
        headers={
            'Content-Type': 'application/vnd.4thoffice.notification.action.list.updated-v5.8+json',
            'Accept': 'application/vnd.4thoffice.notification.action.list.updated-v5.8+json',
            'Authorization': access_token
        },
        data=json.dumps(data)
    )
    return response
