from flask import Blueprint, jsonify, request
import uuid

edit_blueprint = Blueprint('edit', __name__, url_prefix='/events/edit')

@edit_blueprint.route('edit_plan', methods=['POST'])
def edit_plan():
    data = request.get_json()
    if not data:
        return jsonify({"error" : "Invalid JSON Format"}), 400
    
    event_uuid = data.get("event_uuid")

    if not event_uuid:
        return jsonify({"error" : "Missing Event UUID Field"}), 400
    
    name = data.get("name")
    desc = data.get("description")
    start_date = data.get("start_date")
    start_time = data.get("start_time")
    event_address = data.get("event_address")

    # PULL FROM DB USING UUID

    # INSERT INTO DB IF VALUES ARE NOT NULL/None

    return jsonify({"response" : "DB Updated"}), 200
    

    