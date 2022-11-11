from flask import Blueprint
from flask import request


from controllers.candidateController import CandidateController

candidate_blueprint = Blueprint('candidate_blueprint', __name__)
candidate_controller = CandidateController()


@candidate_blueprint.route("/candidate/all", methods=['GET'])
def get_candidates():
    """

    :return:
    """
    response = candidate_controller.index()
    return response, 200


@candidate_blueprint.route("/candidate/<string:id_>", methods=['GET'])
def get_candidate_by_id(id_):
    """

    :param id_:
    :return:
    """
    response = candidate_controller.show(id_)
    return response, 200

@candidate_blueprint.route("/candidate/insert", methods=['POST'])
def insert_candidate():
    """

    :return:
    """
    candidate = request.get_json()
    response = candidate_controller.create(candidate)
    return  response, 201

@candidate_blueprint.route("/candidate/update", methods=['PATCH'])
def update_candidate(id_):
    """

    :param id_:
    :return:
    """
    candidate = request.get_json()
    response = candidate_controller.update(id_, candidate)
    return response, 201


@candidate_blueprint.route("/candidate/delete", methods=['DELETE'])
def delete_candidate(id_):
    """

    :param id_:
    :return:
    """
    response = candidate_controller.delete(id_)
    return response, 204




