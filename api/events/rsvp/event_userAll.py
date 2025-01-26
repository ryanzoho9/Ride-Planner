from flask import Blueprint, jsonify, request
import os
import psycopg2
from dotenv import load_dotenv
import json

load_dotenv()


def event_allUser(event_uuid):
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
                    SELECT * FROM users WHERE event_id = %s
                    """,
            (event_uuid,),
        )
        colnames = [desc[0] for desc in cur.description]
        rows = cur.fetchall()
        result = [dict(zip(colnames, row)) for row in rows]
        json_result = json.dumps(result, default=str)
        conn.commit()
        conn.close()
        return json_result

    except Exception as e:
        return {"error": f"Database error: {str(e)}"}
    
def get_events(event_uuid):
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
            """SELECT * FROM events WHERE event_id = %s""",
            (event_uuid,),
        )
        colnames = [desc[0] for desc in cur.description]
        rows = cur.fetchall()
        result = [dict(zip(colnames, row)) for row in rows]
        json_result = json.dumps(result, default=str)
        conn.commit()
        conn.close()
        return json_result
    except Exception as e:
        return {"error": f"Database error: {str(e)}"}
