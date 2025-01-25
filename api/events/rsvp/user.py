from flask import Blueprint, jsonify, request
import uuid

user_blueprint = Blueprint('user', __name__, url_prefix='/events/rsvp')

@user_blueprint.route('/create_user', methods=['POST'])
def create_event():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON Format"}), 400
    
    name = data.get("name")
    address = data.get("address", "N/A")
    phone_nuber = data.get("phone_number", "N/A")

    if not name:
        return jsonify({"error" : "Missing Name Field"}), 400
    
    # INSERT INFO INTO DB ONCE INITIALIZED

    eventUUID = str(uuid.uuid4())
    return jsonify({"uuid": eventUUID}), 200