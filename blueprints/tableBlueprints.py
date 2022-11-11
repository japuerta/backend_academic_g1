from flask import Blueprint
from flask import request

from controllers.tableController import TableController

table_blueprint = Blueprint('table_blueprint', __name__)
table_controller = TableController()


@table_blueprint.route("/table/all", methods=['GET'])
def get_tables():
    """

    :return:
    """
    response = table_controller.index()
    return response, 200


@table_blueprint.route("/table/<string:id_>", methods=['GET'])
def get_table_by_id(id_):
    """

    :param id_:
    :return:
    """
    response = table_controller.show(id_)
    return response, 200


@table_blueprint.route("/table/insert", methods=['POST'])
def insert_table():
    """

    :return:
    """
    table = request.get_json()
    response = table_controller.create(table)
    return response, 201


@table_blueprint.route("/table/update/<string:id_>", methods=['PATCH'])
def update_table(id_):
    """

    :return:
    """
    table = request.get_json()
    response = table_controller.update(id_, table)
    return response, 201


@table_blueprint.route("/table/delete", methods=['DELETE'])
def delete_table(id_):
    """

    :param id_:
    :return:
    """
    return table_controller.delete(id_), 204



