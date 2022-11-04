import json

from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from waitress import serve


app = Flask(__name__)
cors = CORS(app)


@app.route("/", methods=['GET'])
def home():
    json_ = {"message": "wellcome to academic microservices..."}
    return jsonify(json_)


# config and execute app
def load_file_config():
    with open("config.json") as file:
        data = json.load(file)
    return data


if __name__ == '__main__':
    data_config = load_file_config()
    print("Server runing: http://"+data_config.get('url-backend')+":"+str(data_config.get('port')))
    serve(app, host=data_config.get('url-backend'), port=data_config.get('port'))
