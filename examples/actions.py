import json
import requests
from snapp_email import ApiClient
from snapp_email.datacontract import classes
import examples.config as config
import examples.login as login


def create_actions_http(action_id, action_name, post_id, impersonate_user_id, access_token):
    url = '{}/reminder'.format(
        config.API_URL)

    # example is only for one action, you can append more to ActionList though
    data = {
        'Resource':
            {
                'Id': post_id
            },
        'ActionList':
        [
            {
                '$type': 'Action_18',
                'Id': action_id,
                'Name': action_name,
                'ActionType': 'Positive',
                'AssistantEmail': config.INTEGRATION_KEY,
                'Description': action_name
            },
        ]
    }

    response = requests.post(
        url=url,
        headers={
            'Content-Type': 'application/vnd.4thoffice.reminder.base-v5.18+json',
            'Accept': 'application/vnd.4thoffice.reminder.base-v5.18+json',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US;q=1',
            'Authorization': access_token,
            'X-Impersonate-User': impersonate_user_id
        },
        data=json.dumps(data)
    )
    return response


def delete_actions_http(reminder_id, impersonate_user_id, access_token):
    url = '{}/reminder/{}'.format(config.API_URL, reminder_id)

    response = requests.delete(
        url=url,
        headers={
            'Content-Type': 'application/vnd.4thoffice.reminder.base-v5.18+json',
            'Accept': 'application/vnd.4thoffice.reminder.base-v5.18+json',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US;q=1',
            'Authorization': access_token,
            'X-Impersonate-User': impersonate_user_id
        },
    )
    return response


def create_action_sdk(action_id, action_name, post_id, impersonate_user_id):
    api_client = ApiClient(username=config.INTEGRATION_KEY,
                           password=config.INTEGRATION_SECRET,
                           auth_type=7,
                           api_url=config.API_URL)

    post_obj = classes.ResourceBase_13(Id=post_id)

    # example is only for one action, you can append more to ActionList though
    actions = []
    action = classes.Action_18()
    action.set_Id(action_id)
    action.set_Name(action_name)
    action.set_ActionType('Positive')
    action.set_AssistantEmail(config.INTEGRATION_KEY)
    action.set_Description(action_name)
    actions.append(action)

    reminder_obj = classes.Reminder_22()
    reminder_obj.set_Resource(post_obj)
    reminder_obj.set_ActionList(classes.ListOfActions_18(actions))

    response = api_client.reminder.Reminder_22.create(reminder_obj, impersonate_user_id=impersonate_user_id)
    return response


def delete_action_sdk(reminderId, impersonate_user_id):
    api_client = ApiClient(username=config.INTEGRATION_KEY,
                           password=config.INTEGRATION_SECRET,
                           auth_type=7,
                           api_url=config.API_URL)

    response = api_client.reminder.Reminder_22.delete(reminderId, impersonate_user_id=impersonate_user_id)
    return response
