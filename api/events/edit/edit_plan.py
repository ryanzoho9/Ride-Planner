from flask import Blueprint, jsonify, request
import psycopg2
from services.api_calls import geocoding
import os

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

    try:
        (x_coord, y_coord) = geocoding(event_address)
    except Exception as e:
        return jsonify({"error" : "Invalid Address"}), 400
    
    if not (event_name and desc and start_date and start_time and event_address):
        return jsonify({"error": "Missing Field"}), 400
    # PULL FROM DB USING UUID
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASS")
    db_name = os.getenv("DB_NAME")
    
    try:
        conn = psycopg2.connect(
            host=db_host,
            dbname=db_name,
            user=db_user,
            password=db_pass,
            port=db_port
        )
        cur = conn.cursor()
        
        cur.execute("""
                    UPDATE events 
                    SET event_name = %s, description = %s, start_date = %s, start_time = %s, event_address = %s
                    WHERE event_id = EVENT_ID_PARAM
                    """, (event_uuid, event_name, desc, start_date, start_time, x_coord, y_coord, event_address))
        
        conn.commit()
        cur.close()
        conn.close()
            
    # INSERT INTO DB IF VALUES ARE NOT NULL/None

    return jsonify({"response" : "DB Updated"}), 200
