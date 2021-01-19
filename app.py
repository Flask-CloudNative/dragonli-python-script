import json
from flask import Flask, request, abort
from rainbond_python.parameter import Parameter
from rainbond_python.db_connect import DBConnect
from rainbond_python.error_handler import error_handler

app = Flask(__name__)
error_handler(app)
db = DBConnect(db='dragonli', collection='scripts')


@app.route('/api/1.0/script', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_script():
    parameter = Parameter(request)

    if parameter.method == 'GET':
        response = db.find_paging(parameter)
        return response

    elif parameter.method == 'POST':
        if parameter.verification(checking=parameter.param_json, verify={'title': str, 'script': str}):
            param = parameter.param_json
            insert_dict = {'title': param['title'], 'script': param['script']}
            if db.write_one_docu(docu=insert_dict):
                return '新编排剧本被创建', 201, []
            else:
                abort(500)
        else:
            abort(400)

    elif parameter.method == 'PUT':
        return json.dumps(parameter.param_json, ensure_ascii=False), 200, []

    elif parameter.method == 'DELETE':
        return json.dumps(parameter.param_json, ensure_ascii=False), 200, []


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
