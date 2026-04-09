from flask import Flask, request
import mysql.connector
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def create_db():
    while True:
        try:
            conn = mysql.connector.connect(
                host="db",
                user="root",
                password="root"
            )
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS testdb")
            conn.close()
            break
        except:
            time.sleep(2)

def get_db():
    while True:
        try:
            return mysql.connector.connect(
                host="db",
                user="root",
                password="root",
                database="testdb"
            )
        except:
            time.sleep(2)

@app.route('/save', methods=['POST'])
def save():
    data = request.json
    name = data['name']

    create_db()  # 🔥 important

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS users (name VARCHAR(50))")
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    conn.commit()

    return "Saved!"

app.run(host='0.0.0.0', port=5000)