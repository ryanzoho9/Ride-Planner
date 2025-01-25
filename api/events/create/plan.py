from flask import Blueprint, jsonify, request
from services.uuid_generator import get_uuid
from dotenv import load_dotenv
from services.api_calls import geocoding
from database.connect_db import get_db_connection
import psycopg2
import os

load_dotenv()
create_blueprint = Blueprint('create', __name__, url_prefix='/events/create')

@create_blueprint.route('create_plan', methods=['POST'])
def create_plan():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON Format"}), 400
    
    event_name = data.get("event_name")
    desc = data.get("description")
    start_date = data.get("start_date")
    start_time = data.get("start_time")
    event_address = data.get("event_address")

    try:
        (x_coord, y_coord) = geocoding(event_address)
    except Exception as e:
        return jsonify({"error" : "Invalid Address"}), 400

    if not (event_name and desc and start_date and start_time and event_address):
        return jsonify({"error" : "Missing Field"}), 400

    event_uuid = get_uuid()

    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # Insert event data into the database
        cur.execute("""
            INSERT INTO events (event_id, event_name, description, start_date, start_time, x_coord, y_coord, event_address)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (event_uuid, event_name, desc, start_date, start_time, x_coord, y_coord, event_address))

        # Commit the transaction
        conn.commit()
        
        # Close the cursor and connection
        cur.close()
        conn.close()

        # Return success response
        return jsonify({"event_uuid": event_uuid}), 200

    except Exception as e:
        # Handle database errors
        return jsonify({"error": f"Database error: {str(e)}"}), 500