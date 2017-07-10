import json
import requests
from snapp_email import ApiClient
from snapp_email.datacontract import classes
import examples.config as config
import examples.login as login
import datetime


def get_agenda_sdk(start_datetime, end_datetime=None, size=100, offset=0, impersonate_user_id=None):
    api_client = ApiClient(username=config.INTEGRATION_KEY,
                           password=config.INTEGRATION_SECRET,
                           auth_type=7,
                           api_url=config.API_URL)
    agenda = api_client.appointment.ListOfAgendaPage_22.get(None, start_datetime, size, offset, end_datetime, impersonate_user_id)
    return agenda


def get_agenda_for_next_month_sdk():
    return get_agenda_sdk(datetime.datetime.today(), datetime.datetime.today() + datetime.timedelta(30))
