import os
from dotenv import load_dotenv
import psycopg2
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"status": "working", "message": "Hey homelab!"})

@app.route("/db-test", methods=["GET"])
def dtbase():
    try:
        conn = psycopg2.connect(
                dbname = os.getenv("DB_NAME"),
                user = os.getenv("DB_USER"),
                password = os.getenv("DB_PASSWORD"),
                host = 'psqldatabases',
                port = '5432',
                connect_timeout = 3
        )

        cursor = conn.cursor()

        cursor.execute("SELECT 1;")

        result = cursor.fetchone()
        cursor.close()
        conn.close()

        return jsonify({"database": "connected"})

    except Exception as e:
        return jsonify({"database": "error", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(host='10.0.2.15', port=5000)
