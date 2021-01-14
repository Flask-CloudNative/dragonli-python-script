import json
from flask import Flask, request
from rainbond_python.parameter import Parameter

app = Flask(__name__)


@app.route('/api/1.0/script', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_script():
    parameter = Parameter(request)

    if parameter.method == 'GET':
        return json.dumps(parameter.param_url, ensure_ascii=False), 200, []

    elif parameter.method == 'POST':
        return json.dumps(parameter.param_json, ensure_ascii=False), 200, []

    elif parameter.method == 'PUT':
        return json.dumps(parameter.param_json, ensure_ascii=False), 200, []

    elif parameter.method == 'DELETE':
        return json.dumps(parameter.param_json, ensure_ascii=False), 200, []


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
