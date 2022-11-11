from flask import Blueprints
from flask import request

from controllers.politicalPartyController import PoliticalPartyController

politicalParty_blueprints = Blueprints('politicalParty_blueprint', __name__)
politicalParty_controller = PoliticalPartyController()

@politicalParty_blueprints.route("/politicalParty/all,", methods=['GET'])
def get_politicalParty():
    """

    :return:
    """
    response = politicalParty_controller.index()
    return response, 200

@politicalParty_blueprints.route("/politicalParty/<string:id_>,", methods=['GET'])
def get_politicalParty_by_id(id_):
    """

    :param id_:
    :return:
    """
    response = politicalParty_controller.show(id_)
    return response, 200


@politicalParty_blueprints.route("/politicalParty/insert,", methods=['POST'])
def insert_politicalParty():
    """

    :return:
    """
    politicalParty = request.get_json()
    response = politicalParty_controller.create(politicalParty)
    return response, 201


@politicalParty_blueprints.route("/politicalParty/update/<string:id_>", methods=['PATCH'])
def update_politicalParty(id_):
    """

    :param id_:
    :return:
    """
    politicalParty = request.get_json()
    response = politicalParty_controller.update(id, politicalParty)
    return response, 201


@politicalParty_blueprints.route("/politicalParty/delete/<string:id_>", methods=['DELETE'])
def delete_politicalDepartment(id_):
    """

    :param id_:
    :return:
    """
    response = politicalParty_controller.delete(id_)
    return response, 204
