from flask import Blueprint, jsonify, request
import psycopg2
from services.api_calls import geocoding
import os
import asyncio
import websockets
from dotenv import load_dotenv

load_dotenv()

# edit_blueprint = Blueprint("edit", __name__, url_preix="/events/edit")

# @edit_blueprint.route("driver_update", methods=["POST"])
# def driver_update():
#     data = request.get_json()
#     if not data:
#         return jsonify({"error": "Invalid JSON Format"}), 400

#     driver_update = data.get("driver_update")

#     if not driver_update:
#         return jsonify({"Error": "Missing Driver Update"}), 400

#     if driver_update == "No":


async def handle_client(websocket, path):
    try:
        async for message in websocket:
            data = json.loads(message)

            action = data.get("action")
            cargoing_id = data.get("cargoing_id")

            if action == "remove_driver" and cargoing_id:
                result = await remove_driver_from_db(cargoing_id)
                await websocket.send(
                    json.dumps({"status": "success", "message": result})
                )
            else:
                await websocket.send(
                    json.dumps(
                        {
                            "status": "error",
                            "message": "Invalid action or missing cargoingin_id",
                        }
                    )
                )
    except Exception as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500


async def remove_driver_from_db(cargoing_id):
    cargoing_id = cargoing_id
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
                    UPDATE users SET carownid = NULL, cargoin_id = -1 WHERE cargoing_id = %s
                    """,
            (cargoing_id,),
        )
        cur.execute(
            """
                    DELETE FROM cars WHERE car_id = %s
                    """,
            (cargoing_id,),
        )
        conn.commit()
        cur.close()
        conn.close()

        return "MAYBE THIS IS RETURNED"  # NEED TO ADD
    except Exception as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500


async def start_server():
    server = await websockets.serve(handle_client, "localhost", 8765)
    print("WebSocket server started at ws://localhost:8765")
    await server.wait_closed()
