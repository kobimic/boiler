import json
from flask import jsonify, request, Blueprint

routes = Blueprint('routes', __name__)


@routes.route("/", methods=["GET"])
def root():
    return jsonify({"msg": "root"}), 200



@routes.route("/say_hello", methods=["GET"])
def say_hello():
    return jsonify({"msg": "hello"}), 200


@routes.route("/set_hello", methods=["POST"])
def set_hello():
    return jsonify({"msg": "hello"}), 200


@routes.route("/say_hello/<id>/complete", methods=["POST"])
def say_hello_id(id):
    id = int(id)
    return jsonify({'msg': f'order id:{id} invalid/missing'}), 200
