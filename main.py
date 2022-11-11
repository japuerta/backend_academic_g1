import json

from flask import Flask
from flask import jsonify
from flask_cors import CORS
from waitress import serve

from blueprints.candidateBlueprints import candidate_blueprint

app = Flask(__name__)
cors = CORS(app)
app.register_blueprint(candidate_blueprint)


@app.route("/", methods=['GET'])
def home():
    response = {"message": "wellcome to academic microservices G1..."}
    return jsonify(response)


# config and execute app
def load_file_config():
    with open("config.json") as file:
        data = json.load(file)
    return data


if __name__ == '__main__':
    data_config = load_file_config()
    print("Server running: http://"+data_config.get('url-backend')+":"+str(data_config.get('port')))
    serve(app, host=data_config.get('url-backend'), port=data_config.get('port'))
