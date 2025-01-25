from flask import Blueprint, jsonify, request
import uuid

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/dummyAPI', methods=['GET'])
def dummyAPI():
    return jsonify({
        "app" : "Ride Planner",
        "dummy_data" : "random stuff for testing"
    })