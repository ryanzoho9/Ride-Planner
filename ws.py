import json
from database.connect_db import get_db_connection
from services.uuid_generator import get_uuid
from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

def updateDriver(user_id, cargoin_id):
    try:
        if cargoin_id != -1:
            cargoin_id = addDriver("Yes")
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            UPDATE users
            SET carown_id = %s, cargoinid = %s
            WHERE user_id = %s
            """, (cargoin_id, cargoin_id, user_id))

        conn.commit()
        cur.close()
        conn.close()
        return json.dumps({"message": "Driver details updated successfully"}), 200
    except Exception as e:
        return json.dumps({"error": f"Database error: {str(e)}"}), 500

def addPerson(user_uuid, car_owner, cargoin_id, name, x_coord, y_coord, phone_number, event_id):
    try:
        conn = get_db_connection()
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

        return json.dumps({"user_uuid": user_uuid}), 200

    except Exception as e:
        return json.dumps({"error": f"Database error: {str(e)}"}), 500

def addDriver(car_owner):
    def createCar(car_uuid):
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO cars(car_id, seats_available, passengers)
                VALUES (%s, 4, 1)
                """, (car_uuid,))
            conn.commit()
            cur.close()
            conn.close()
        except Exception as e:
            return json.dumps({"error": f"Database error: {str(e)}"})

    if car_owner == "No":
        car_owner = None
        cargoin_id = -1
    else:
        car_owner = get_uuid()
        cargoin_id = car_owner
        createCar(car_owner)
    return cargoin_id

def removePassenger(user_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            UPDATE users
            SET cargoinid = -1
            WHERE user_id = %s
            """, (user_id,))

        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        return json.dumps({"error": f"Database error: {str(e)}"})

def addPassenger(user_id, cargoin_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            UPDATE users
            SET cargoinid = %s
            WHERE user_id = %s
            """, (cargoin_id, user_id,))

        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        return json.dumps({"error": f"Database error: {str(e)}"})

def removeDriver(cargoin_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            UPDATE users
            SET cargoinid = -1, carown_id = -1
            WHERE cargoinid = %s
            """, (cargoin_id,))

        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        return json.dumps({"error": f"Database error: {str(e)}"})

def displayCars():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # Fetch all users with carown_id not null
        cur.execute("""
            SELECT * FROM users
            WHERE carown_id IS NOT NULL
        """)

        rows = cur.fetchall()
        carown_ids = [row[1] for row in rows]  # Adjust indices based on schema
        carowner_names = [row[3] for row in rows]  # Adjust indices based on schema

        if not carown_ids:
            print("No cars found.")
            return json.dumps({"error": "No cars found"}), 404

        print("Car Owner IDs:", carown_ids)
        print("Car Owner Names:", carowner_names)

        passengers = getPassengersFromCars(carown_ids)

        if isinstance(passengers, dict) and "error" in passengers:
            return json.dumps(passengers), 500

        if len(carowner_names) != len(passengers):
            print("Mismatch between car owners and passengers.")
            return json.dumps({"error": "Mismatch between car owners and passengers"}), 500

        data = {}
        for i, name in enumerate(carowner_names):
            data[name] = passengers[i] if i < len(passengers) else []

        return json.dumps(data)

    except Exception as e:
        print("Exception occurred in displayCars:", e)
        return json.dumps({"error": f"Database error: {str(e)}"}), 500

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def getPassengersFromCars(carown_ids):
    all_passengers = []
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        for carown_id in carown_ids:
            print(f"Fetching passengers for car owner ID: {carown_id}")
            cur.execute("""
                SELECT * FROM users
                WHERE carown_id IS NULL AND cargoinid = %s
            """, (carown_id,))
            rows = cur.fetchall()
            listOfPassengers = [row[3] for row in rows]  # Adjust index based on schema
            all_passengers.append(listOfPassengers)

        print("All passengers fetched:", all_passengers)
        return all_passengers

    except Exception as e:
        print("Exception occurred in getPassengersFromCars:", e)
        return {"error": f"Database error: {str(e)}"}

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

# Test examples (comment/uncomment as needed)
# addPerson('user999', None, None, 'Some Bastard 2', 93.342, 71.234, '1234567890', '5b120ad8-2899-4f6a-84ba-63f21e0c7d59')
# addPassenger('user555', 'c9625549-a530-482c-a9c0-7eefba86d861')
# removeDriver('c9625549-a530-482c-a9c0-7eefba86d861')

print(displayCars())
