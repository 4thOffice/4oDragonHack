from snapp_email import ApiClient
from snapp_email.datacontract import classes
import examples.config as config
from examples.create_post import create_user_object_from_email
import examples.login as login


def get_groups_for_user(impersonate_user_id=None):
    api_client = ApiClient(username=config.INTEGRATION_KEY,
                           password=config.INTEGRATION_SECRET,
                           auth_type=7,
                           api_url=config.API_URL)
    groups = api_client.navigation.Menu_22.get(None, 100, 0, groupStreamOnly=True,
                                               impersonate_user_id=impersonate_user_id)
    return groups


def create_group(name, admins=[], members=[], description=None, impersonate_user_id=None):
    api_client = ApiClient(username=config.INTEGRATION_KEY,
                           password=config.INTEGRATION_SECRET,
                           auth_type=7,
                           api_url=config.API_URL)
    group_obj = classes.Group_17(Description=description)
    group_obj.set_Name(name)
    admin_list = []
    member_list = []
    for email in admins:
        admin_list.append(create_user_object_from_email(email))
    for email in members:
        member_list.append(create_user_object_from_email(email))
    group_obj.set_Administrators(classes.ListOfUsers_14(admin_list))
    group_obj.set_Members(classes.ListOfUsers_14(member_list))
    group = api_client.group.Group_17.create(group_obj, impersonate_user_id=impersonate_user_id)
    return group


get_groups_for_user()