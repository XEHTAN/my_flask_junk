from models import Role
from typing import List
from flask import jsonify



class RoleSerializer():

    @staticmethod
    def serialize_one(data: Role):
        response = {'id': data.id, 'name': data.name}
        return jsonify(response)

    @staticmethod
    def serialize_many(data_collection):
        data_list = []

        for datum in data_collection:
            data_list.append(serialize_one(datum))
        return jsonify(data_list)
