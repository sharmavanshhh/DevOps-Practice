from flask import Flask
import mysql.connector
import time

app = Flask(__name__)

def create_database():
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

def get_db_connection():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="testdb"
    )

@app.route('/')
def home():
    try:
        create_database()
        conn = get_db_connection()
        return "Flask + MySQL DB Running...!! "
    except Exception as e:
        return f"Error: {str(e)}"

app.run(host='0.0.0.0', port=5000)