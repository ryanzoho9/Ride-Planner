from flask import Blueprint, jsonify

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/dummyAPI', methods=['GET'])
def dummyAPI():
    return jsonify({
        "app" : "Virtual Real Estate Agent",
        "dummy_data" : "random stuff for testing"
    })