from flask_socketio import SocketIO, emit
from database.connect_db import get_db_connection
import json

def register_websocket_handlers(socketio: SocketIO):
    @socketio.on('rsvp')
    def handle_rsvp(data):
        # Insert RSVP data into the database
        try:
            conn = get_db_connection()
            cur = conn.cursor()

            cur.execute(
                """
                UPDATE users
                SET CarGoInId = %s
                WHERE user_id = %s
                """,
                (data['car_go_in_id'], data['user_id'])
            )

            conn.commit()
            cur.close()
            conn.close()

            emit('rsvp_update', data, broadcast=True)
        except Exception as e:
            raise Exception("Database Failed")

    @socketio.on('assign_driver')
    def handle_driver_assignment(data):
        try:
            conn = get_db_connection()
            cur = conn.cursor()

            cur.execute(
                """
                UPDATE users
                SET CarOwn_id = %s
                WHERE user_id = %s
                """,
                (data['user_id'], data['user_id'])
            )

            conn.commit()
            cur.close()
            conn.close()

            emit('assign_update', {'user_id': data['user_id'], 'role': 'driver'}, broadcast=True)
        except Exception as e:
            raise Exception("Database Failed")
        
    @socketio.on('assign_rider')
    def handle_rider_assignment(data):
        try:
            conn = get_db_connection()
            cur = conn.cursor()

            cur.execute(
                """
                UPDATE users
                SET CarGoInId = %s
                WHERE user_id = %s
                """,
                (data['car_id'], data['user_id'])
            )

            conn.commit()
            cur.close()
            conn.close()

            emit('assign_update', {'user_id': data['user_id'], 'car_id': data['car_id'], 'role': 'rider'}, broadcast=True)
        except Exception as e:
            raise Exception("Database Failed")
