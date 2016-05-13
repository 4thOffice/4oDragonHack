import json

from bson import json_util
from flask import Blueprint, request

from smart_assistant_example.models.action import action_from_json

bp = Blueprint('action', __name__)


@bp.route('/action', methods=['POST'])
def set_action():
    data = json.loads(request.data.decode('utf-8'))

    args = request.args
    user_id = args.get('userId')

    action = action_from_json(data['ActionList'][0])
    actionable_resource = action()
    response = actionable_resource.to_json()
    return json.dumps(response, default=json_util.default), 200, {'Content-Type': 'application/vnd.4thoffice.actionable.resource-v5.17+json'}
