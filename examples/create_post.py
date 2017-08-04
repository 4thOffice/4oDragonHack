import json
import requests
from snapp_email import ApiClient
from snapp_email.datacontract import classes
import examples.config as config
import examples.login as login
import datetime


def create_card_http(to_user_email, title, content, access_token, attachment_names_ids=None):
    data = {
            'Name': title,
            'Text': content,
            'ShareList': [
                {
                    '$type': 'User_14',
                    'AccountList': [
                        {
                            '$type': 'AccountEmail_14',
                            'Email': to_user_email
                        }
                    ]
                }
            ]
        }
    if attachment_names_ids:
        data['Files'] = [
                {
                    '$type': 'File_14',
                    'Id': attachment_id,
                    'Name': attachment_name
                } for attachment_name, attachment_id in attachment_names_ids
            ]

    url = '{}/post'.format(config.API_URL)

    response = requests.post(
        url=url,
        headers={
            'Content-Type': 'application/vnd.4thoffice.post-5.18+json',
            'Accept': 'application/vnd.4thoffice.post-5.18+json',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US;q=1',
            'Authorization': access_token
        },
        data=json.dumps(data)
    )

    return response


def create_card_html_http(to_user_email, title, html_content, access_token, attachment_ids=None, inline_attachment_ids=None):
    data = {
        'Name': title,
        'BodyHtml': html_content,
        'ShareList': [
            {
                '$type': 'User_14',
                'AccountList': [
                    {
                        '$type': 'AccountEmail_14',
                        'Email': to_user_email
                    }
                ]
            }
        ]
    }

    if attachment_ids is not None or inline_attachment_ids is not None:
        data['Files'] = []

    if attachment_ids:
        attachments = [
            {
                '$type': 'File_14',
                'Id': attachment_id,
                'Name': attachment_name
            } for attachment_name, attachment_id in attachment_ids
            ]
        data['Files'] += attachments

    if inline_attachment_ids:
        inline_attachments = [
            {
                '$type': 'File_14',
                'Id': attachment_id,
                'Name': attachment_name,
                'Hidden': True
            } for attachment_name, attachment_id in inline_attachment_ids
            ]
        data['Files'] += inline_attachments

    url = '{}/post'.format(config.API_URL)

    response = requests.post(
        url=url,
        headers={
            'Content-Type': 'application/vnd.4thoffice.post-5.18+json',
            'Accept': 'application/vnd.4thoffice.post-5.18+json',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US;q=1',
            'Authorization': access_token
        },
        data=json.dumps(data)
    )

    return response


def create_reply_http(card_id, content, access_token, attachment_names_ids=None):
    data = {
        'Parent': {
            'Id': card_id
        },
        'Text': content
    }

    if attachment_names_ids:
        data['Files'] = [
                {
                    '$type': 'File_14',
                    'Id': attachment_id,
                    'Name': attachment_name
                } for attachment_name, attachment_id in attachment_names_ids
            ]

    url = '{}/post'.format(config.API_URL)
    response = requests.post(
        url=url,
        headers={
            'Content-Type': 'application/vnd.4thoffice.post-5.18+json',
            'Accept': 'application/vnd.4thoffice.post-5.18+json',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US;q=1',
            'Authorization': access_token
        },
        data=json.dumps(data)
    )
    return response


def post_attachment_http(document_name, document_path, access_token):
    with open(document_path, 'rb') as file:
        document = file.read()

    url = '{}/document'.format(config.API_URL)

    response = requests.post(
        url=url,
        headers={
            'Accept': 'application/vnd.4thoffice.document-v4.0+json',
            'Content-Type': 'application/octet-stream',
            'X-Upload-File-Name': document_name,
            'Authorization': access_token
        },
        data=document
    )

    return response


def create_card_sdk(to_user_email, title, content, attachment_names_ids=None):
    api_client = ApiClient(username=config.INTEGRATION_KEY,
                           password=config.INTEGRATION_SECRET,
                           auth_type=7,
                           api_url=config.API_URL)
    share_list = []
    share_list.append(create_user_object_from_email(to_user_email))
    share_list = classes.ListOfResources_13(share_list)

    post_obj = classes.Post_22(Text=content, ShareList=share_list)
    if attachment_names_ids:
        files = []
        for attachment_id in attachment_names_ids:
            file = classes.File_14()
            file.set_Id(attachment_id)
            files.append(file)
        post_obj.set_Files(classes.ListOfFiles_14(files))
    post_obj.set_Name(title)
    created_post = api_client.post.Post_22.create(post_obj)

    return created_post


def create_card_html_sdk(to_user_email, title, content, attachment_names_ids=None):
    api_client = ApiClient(username=config.INTEGRATION_KEY,
                           password=config.INTEGRATION_SECRET,
                           auth_type=7,
                           api_url=config.API_URL)
    share_list = []
    share_list.append(create_user_object_from_email(to_user_email))
    share_list = classes.ListOfResources_13(share_list)

    post_obj = classes.Post_22(BodyHtml=content, ShareList=share_list)
    if attachment_names_ids:
        files = []
        for attachment_id in attachment_names_ids:
            file = classes.File_14()
            file.set_Id(attachment_id)
            files.append(file)
        post_obj.set_Files(classes.ListOfFiles_14(files))
    post_obj.set_Name(title)
    created_post = api_client.post.Post_22.create(post_obj)

    return created_post


def create_reply_sdk(card_id, content, attachment_names_ids=None):
    api_client = ApiClient(username=config.INTEGRATION_KEY,
                           password=config.INTEGRATION_SECRET,
                           auth_type=7,
                           api_url=config.API_URL)
    parent = classes.DiscussionBase_22()
    parent.set_Id(card_id)
    post_obj = classes.Post_22(Text=content, Parent=parent)
    # TODO if False: post_obj = Post_22(BodyHtml=html)
    if attachment_names_ids:
        files = []
        for attachment_id in attachment_names_ids:
            file = classes.File_14()
            file.set_Id(attachment_id)
            files.append(file)
        post_obj.set_Files(classes.ListOfFiles_14(files))

    created_post = api_client.post.Post_22.create(post_obj)
    return created_post


def create_user_object_from_email(email):
    return classes.User_14(
        AccountList=classes.ListOfAccounts_14([
            classes.AccountEmail_14(email)
        ])
    )


def create_group_object_from_id(group_id):
    group = classes.Group_17()
    group.set_Id(group_id)
    return group


def create_card_html_to_group_with_share_only_members(group_id,
                                                      to_user_email,
                                                      title,
                                                      content,
                                                      attachment_names_ids=None):
    api_client = ApiClient(username=config.INTEGRATION_KEY,
                           password=config.INTEGRATION_SECRET,
                           auth_type=7,
                           api_url=config.API_URL)
    share_list = []
    share_list.append(create_user_object_from_email(to_user_email))
    share_list.append(create_group_object_from_id(group_id))
    share_list = classes.ListOfResources_13(share_list)

    post_obj = classes.Post_22(BodyHtml=content, ShareList=share_list)
    if attachment_names_ids:
        files = []
        for attachment_id in attachment_names_ids:
            file = classes.File_14()
            file.set_Id(attachment_id)
            files.append(file)
        post_obj.set_Files(classes.ListOfFiles_14(files))
    post_obj.set_Name(title)
    created_post = api_client.post.Post_22.create(post_obj)

    return created_post