from flask import Blueprint
from flask import request

from controllers.candidateController import CandidateController

candidate_blueprint = Blueprint('candidate_blueprint', __name__)
candidate_controller = CandidateController()


@candidate_blueprint.route("/candidate/all", methods=['GET'])
def get_candidates():
    response = candidate_controller.index();
    return response, 200



