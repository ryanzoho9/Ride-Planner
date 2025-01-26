from flask import Blueprint, jsonify, request
from services.uuid_generator import get_uuid
from services.api_calls import geocoding
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

    if car_owner == "No":
        car_owner = None
        cargoin_id = -1

    if car_owner == "Yes":
        car_owner = get_uuid()
        cargoin_id = car_owner
        createCar(car_owner)    

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

    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASS")
    db_name = os.getenv("DB_NAME")

    try:
        conn = psycopg2.connect(
            host=db_host, dbname=db_name, user=db_user, password=db_pass, port=db_port
        )
        cur = conn.cursor()
        cur.execute(
            """
                        INSERT INTO users(user_id, carown_id, cargoinid, name, x_coord, y_coord, phone_number, event_id)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        """,
            (
                user_uuid,
                car_owner,
                cargoin_id,
                name,
                x_coord,
                y_coord,
                phone_number,
                event_id,
            ),
        )

        conn.commit()
        cur.close()
        conn.close()

        return jsonify({"user_uuid": user_uuid}), 200

    except Exception as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500


def createCar(car_uuid):
    
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASS")
    db_name = os.getenv("DB_NAME")

    try:
        conn = psycopg2.connect(
            host=db_host, dbname=db_name, user=db_user, password=db_pass, port=db_port
        )
        cur = conn.cursor()
        cur.execute("""
                INSERT INTO cars(car_id, seats_available, passengers)
                VALUES (%s, 4, 1)
                """,(car_uuid,))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500