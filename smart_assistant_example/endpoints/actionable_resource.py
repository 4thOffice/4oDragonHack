import json

from bson import json_util
from flask import Blueprint, request
from flask import abort

import config
from smart_assistant_example.models.action import Action, action_from_json
from smart_assistant_example.models.actionable_resource import ActionableResource

bp = Blueprint('actionable_resource', __name__)


@bp.route('/actionableResource', methods=['GET'])
@bp.route('/actionableResource/<actionable_resource_id>', methods=['GET'])
def actionable_resource(actionable_resource_id=None):
    args = request.args
    user_id = args.get('userId')

    if actionable_resource_id:
        decoded = actionable_resource_id.split('.')
        context_type = decoded[1].lower()
        if len(decoded) == 2:
            context_id = None
        elif len(decoded) == 3:
            context_id = decoded[2]
        else:
            abort(400)

    if context_type == 'StreamListImportant'.lower():
        assistant_chat_bubble = 'Hello and welcome on stream list'

        next_step = Action(name='Show me next thing', type='ActionNextStep_18')
        close_dialog = Action(name='Bye', type='ActionFinishWorkflow_18')
        actions = [next_step, close_dialog]

        description_list = [assistant_chat_bubble]

        actionable_resource = ActionableResource(description_list, actions)
    else:
        return '', 204

    response = actionable_resource.to_json()
    return json.dumps(response, default=json_util.default), 200, {'Content-Type': 'application/vnd.4thoffice.actionable.resource-v5.18+json'}


@bp.route('/actionableResource/availability', methods=['GET'])
def actionable_resource_availability():
    args = request.args
    user_id = args.get('userId')
    context_type = args.get('contextType').lower() if 'contextType' in args else None
    context_id = args.get('contextId')

    if context_type == 'StreamListImportant'.lower():
        availability_mode = 'Action'
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


@bp.route('/action', methods=['POST'])
def set_action():
    data = json.loads(request.data.decode('utf-8'))

    args = request.args
    user_id = args.get('userId')

    action = action_from_json(data['ActionList'][0])
    actionable_resource = action()
    response = actionable_resource.to_json()
    return json.dumps(response, default=json_util.default), 200, {'Content-Type': 'application/vnd.4thoffice.actionable.resource-v5.18+json'}
