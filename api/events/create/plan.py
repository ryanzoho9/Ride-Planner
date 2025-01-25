from flask import Blueprint, jsonify, request
import uuid

create_blueprint = Blueprint('create', __name__, url_prefix='/events/create')

@create_blueprint.route('create_plan', methods=['POST'])
def create_plan():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON Format"}), 400
    
    name = data.get("name")
    desc = data.get("description")
    start_date = data.get("start_date")
    start_time = data.get("start_time")
    event_address = data.get("event_address")

    if not (name and desc and start_date and start_time and event_address):
        return jsonify({"error" : "Missing Field"}), 400
    
    # INSERT INTO DB

    event_uuid = str(uuid.uuid4())
    return jsonify({"event_uuid": event_uuid}), 200