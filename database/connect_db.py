import psycopg2
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        raise
    
    
def initializeDb(QUERY):
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
    cur.execute(QUERY)
    conn.commit()
    conn.close()
except Exception as e:
    return jsonify({"error": f"Database error: {str(e)}"}), 500