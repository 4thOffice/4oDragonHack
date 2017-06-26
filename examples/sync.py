import json
import requests
from snapp_email import ApiClient
import examples.config as config
import examples.login as login
import datetime


def get_latest_since_id_http(notification_type, older_than, token):
    notf_type = 'PostCreated'
    if notification_type:
        notf_type = notification_type

    result = get_notification_sync_http(notification_types=[notf_type],
                                   size=250,
                                   skip_older_than=older_than,
                                   sort_direction='Descending',
                                   access_token=token)

    return result['LastNotificationId']


def get_notification_sync_http(long_polling=False,
                          notification_types=[],
                          offset=0,
                          return_full_resource=False,
                          size=50,
                          skip_older_than=None,
                          sort_direction='Ascending',
                          since_id=None,
                          access_token=None):
    url = '{}/notification'.format(config.API_URL)
    url_parameters = {
        'size': size,
        'offset': offset,
        'LongPolling': long_polling,
        'SortDirection': sort_direction,
        'ReturnFullResource': return_full_resource
    }
    if notification_types is not None and len(notification_types) > 0:
        url_parameters['NotificationType'] = notification_types

    if skip_older_than is not None and type(skip_older_than) is datetime:
        url_parameters['SkipOlderThan'] = skip_older_than.isoformat()

    if since_id is not None:
        url_parameters['SinceId'] = since_id

    token = access_token if access_token is not None else login.login_http()

    response = requests.get(
        url=url,
        headers={
            'Accept': 'application/vnd.4thoffice.notification.list.page-v5.18+json',
            'Authorization': token,
            'User-Agent': config.API_USER_AGENT,
        },
        params=url_parameters
    )

    response.raise_for_status()

    return response.json()


def get_latest_since_id_sdk(older_than):
    result = get_notification_sync_normal_sdk(size=250,
                                              skip_older_than=older_than,
                                              sort_direction='Descending')

    return result.LastNotificationId


def get_notification_sync_normal_sdk(offset=0,
                                     return_full_resource=False,
                                     size=50,
                                     skip_older_than=None,
                                     sort_direction='Ascending',
                                     since_id=None):
    api_client = ApiClient(username=config.INTEGRATION_KEY,
                           password=config.INTEGRATION_SECRET,
                           auth_type=7,
                           api_url=config.API_URL)
    return api_client.notification.ListOfNotificationsPage_22.get_2(size,
                                                                    offset,
                                                                    since_id,
                                                                    sortDirection=sort_direction,
                                                                    returnFullResource=return_full_resource,
                                                                    skipOlderThan=skip_older_than)


def get_notification_sync_long_polling_sdk(long_polling=False,
                          offset=0,
                          return_full_resource=False,
                          size=50,
                          skip_older_than=None,
                          since_id=None):
    api_client = ApiClient(username=config.INTEGRATION_KEY,
                           password=config.INTEGRATION_SECRET,
                           auth_type=7,
                           api_url=config.API_URL)
    return api_client.notification.ListOfNotificationsPage_22.get_3(since_id, size, offset, long_polling, return_full_resource, skip_older_than)
