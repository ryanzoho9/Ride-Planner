from flask import Blueprint, jsonify, request
from services.uuid_generator import get_uuid

user_blueprint = Blueprint('user', __name__, url_prefix='/events/rsvp')

@user_blueprint.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON Format"}), 400
    
    name = data.get("name")
    address = data.get("address", "N/A")
    phone_number = data.get("phone_number", "N/A")

    if not name:
        return jsonify({"error" : "Missing Name Field"}), 400
    
    # INSERT INFO INTO DB ONCE INITIALIZED

    user_uuid = get_uuid()
    return jsonify({"user_uuid": user_uuid}), 200