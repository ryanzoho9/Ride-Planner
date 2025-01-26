from flask import Blueprint, jsonify, request
from services.uuid_generator import get_uuid
from services.api_calls import geocoding
from ws import addDriver, addPerson
import psycopg2
import os
from database import connect_db

user_blueprint = Blueprint("user", __name__, url_prefix="/events/rsvp")


@user_blueprint.route("/create_user", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON Format"}), 400

    name = data.get("name")
    address = data.get("address", "N/A")
    phone_number = data.get("phone_number", "N/A")
    car_owner = data.get("car_owner")
    event_id = data.get("event_id")

    cargoin_id = addDriver(car_owner) 

    if address == "N/A":
        x_coord = None
        y_coord = None
        address = None
    else:
        try:
            (x_coord, y_coord) = geocoding(address)
        except Exception as e:
            return jsonify({"error": "Invalid Address"}), 400

    if phone_number == "N/A":
        phone_number = None

    if not name:
        return jsonify({"error": "Missing Name Field"}), 400

    user_uuid = get_uuid()

    # INSERT INFO INTO DB ONCE INITIALIZED

    try:
        data = addPerson(user_uuid, car_owner, cargoin_id, name, x_coord, y_coord, phone_number, event_id)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500