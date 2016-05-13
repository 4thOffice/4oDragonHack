import json
import os

from API_4o.card import create_card, post_to_existing_card, post_attachment, get_user_chat_id
from API_4o.get_data import get_user_by_email, get_stream, get_group, get_streams_of_user
from API_4o.push_notification import send_push_notification
from smart_assistant_example.models.user import User


def example_send_push_notification(user):

    push_notification_message = 'Hi {}, check what I found for you'.format(user.first_name)
    custom_id = 'Notification.example'
    response = send_push_notification(user.id, custom_id, push_notification_message)

    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)
    return data


def example_get_user_by_email(user_email):
    response = get_user_by_email(user_email)

    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)
    return data


def example_post_new_card(user):
    title = 'Welcome!'
    content = 'Hello {}, this is me, your smart assistant'.format(user.first_name)

    response = create_card(user.email, title, content)

    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)
    return data


def example_post_to_existing_card(user):
    data = example_post_new_card(user)
    card_id = data['Parent']['Id']
    content = 'One more thing, {}'.format(user.first_name)
    response = post_to_existing_card(card_id, content)

    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)
    return data


def example_post_with_attachment(user):
    title = 'Welcome with attachment!'
    content = 'Hello {}, this is me, your smart assistant'.format(user.first_name)
    file_name = '4thOffice.png'
    document_path = '{}{}{}'.format(os.path.dirname(os.path.abspath(__file__)), os.sep, file_name)
    response = post_attachment(file_name, document_path)
    if not 200 < response.status_code < 300:
        response.raise_for_status()

    attachment_id = json.loads(response.text)['Id']
    attachment_names_ids = [(file_name, attachment_id)]

    response = create_card(user.email, title, content, attachment_names_ids)
    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)
    return data


def example_post_chat_message(user):
    response = get_user_chat_id(user.email)
    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)

    card_chat_id = data['Id']

    content = 'Hi {}, this is a chat message ;)'.format(user.name)
    response = post_to_existing_card(card_chat_id, content)
    return response


def example_get_stream(user_id, stream_id):
    response = get_stream(user_id, stream_id)

    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)
    return data


def example_get_group(user_id, group_id):
    response = get_group(user_id, group_id)

    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)
    return data


def example_get_streams_of_user(user):
    response = get_streams_of_user(user.id)

    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)

    frist_stream_id = data['MenuItemList'][0]['Resource']['Id']
    return frist_stream_id


def example_get_groups_of_user(user):
    response = get_streams_of_user(user.id, group_streams_only=True)

    if not 200 < response.status_code < 300:
        response.raise_for_status()

    data = json.loads(response.text)

    frist_stream_id = data['MenuItemList'][0]['Resource']['Id']
    return frist_stream_id


if __name__ == '__main__':
    user_email = 'gaspertestz@gmail.com'
    user = User(example_get_user_by_email(user_email))

    example_send_push_notification(user)

    example_post_new_card(user)

    example_post_to_existing_card(user)

    example_post_with_attachment(user)

    example_post_chat_message(user)

    stream_id = example_get_streams_of_user(user)
    example_get_stream(user.id, stream_id)

    group_id = example_get_groups_of_user(user)
    example_get_group(user.id, group_id)
