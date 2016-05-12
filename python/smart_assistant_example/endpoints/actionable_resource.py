import json

from bson import json_util
from flask import Blueprint, request
from flask import abort

from python.smart_assistant_example import config as config
from python.smart_assistant_example.models.action import Action
from python.smart_assistant_example.models.actionable_resource import ActionableResource

bp = Blueprint('actionable_resource', __name__)


@bp.route('/actionableResource', methods=['GET'])
@bp.route('/actionableResource/<actionable_resource_id>', methods=['GET'])
def actionable_resource(actionable_resource_id=None):
    args = request.args
    user_id = args.get('userId')

    if actionable_resource_id:
        decoded = actionable_resource_id.split('.')
        context_type = decoded[1]
        if len(decoded) == 2:
            context_id = None
        elif len(decoded) == 3:
            context_id = decoded[2]
        else:
            abort(400)

    if context_type == 'ChatStream'.lower():
        assistant_chat_bubble = 'Hello and welcome on chat stream'

        next_step = Action(name='Show me next message', type='ActionNextStep_18', action_type='Positive')
        close_dialog = Action(name='OK, thanks', type='ActionFinishWorkflow_18', action_type='Neutral')
        actions = [next_step, close_dialog]

        description_list = [assistant_chat_bubble]

        actionable_resource = ActionableResource(description_list, actions)
    elif context_type == 'StreamListMuted'.lower():
        return '', 204
    elif context_type == 'GroupList'.lower():
        return '', 204
    elif context_type == 'BoardList'.lower():
        return '', 204
    elif context_type == 'Stream'.lower():
        return '', 204
    elif context_type == 'StreamListImportant'.lower():
        assistant_chat_bubble = 'Hello and welcome on stream list'

        next_step = Action(name='Show me next thing', type='ActionNextStep_18', action_type='Positive')
        close_dialog = Action(name='Bye', type='ActionFinishWorkflow_18', action_type='Neutral')
        actions = [next_step, close_dialog]

        description_list = [assistant_chat_bubble]

        actionable_resource = ActionableResource(description_list, actions)
    elif context_type == 'ReminderList'.lower():
        return '', 204
    elif context_type == 'Notification'.lower():
        assistant_chat_bubble = 'Hello this is from push notification'

        close_dialog = Action(name='Nice', type='ActionFinishWorkflow_18', action_type='Positive')
        actions = [close_dialog]
        description_list = [assistant_chat_bubble]
        actionable_resource = ActionableResource(description_list, actions)
    else:
        return '', 204

    response = actionable_resource.to_json()
    return json.dumps(response, default=json_util.default), 200, {'Content-Type': 'application/vnd.4thoffice.actionable.resource-v5.17+json'}


@bp.route('/actionableResource/availability', methods=['GET'])
def actionable_resource_availability():
    args = request.args
    user_id = args.get('userId')
    context_type = args.get('contextType').lower() if 'contextType' in args else None
    context_id = args.get('contextId')

    if context_type == 'ChatStream'.lower():
        availability_mode = 'Action'
    elif context_type == 'StreamListMuted'.lower():
        availability_mode = 'None'
    elif context_type == 'GroupList'.lower():
        availability_mode = 'None'
    elif context_type == 'BoardList'.lower():
        availability_mode = 'None'
    elif context_type == 'Stream'.lower():
        availability_mode = 'None'
    elif context_type == 'StreamListImportant'.lower():
        availability_mode = 'Action'
    elif context_type == 'ReminderList'.lower():
        availability_mode = 'None'
    elif context_type == 'Notification'.lower():
        availability_mode = 'None'
    else:
        availability_mode = 'None'

    if context_id:
        actionable_resource_id = '{}.{}.{}'.format(config.SMART_ASSISTANT['NAME'], context_type, context_id)
    else:
        actionable_resource_id = '{}.{}'.format(config.SMART_ASSISTANT['NAME'], context_type)

    response = {
        '$type': 'ActionableResourceAvailability_20',
        'Mode': availability_mode,
        'ActionableResourceId': actionable_resource_id
    }
    return json.dumps(response, default=json_util.default), 200, {'Content-Type': 'application/vnd.4thoffice.actionable.resource.availability-v5.15+json'}

