from flask import Flask

import config

app_flask = Flask(__name__)


@app_flask.after_request
def f(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, PUT, POST, DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response


from smart_assistant_example.endpoints import actionable_resource
app_flask.register_blueprint(actionable_resource.bp)


if __name__ == '__main__':
    print('Running smart assistant api...')
    app_flask.run(host=config.SMART_ASSISTANT['API']['HOST'],
                  port=config.SMART_ASSISTANT['API']['PORT'],
                  debug=True,
                  use_reloader=False,
                  threaded=True)
