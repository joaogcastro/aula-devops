from flask import Flask
from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()
app = Flask(__name__)

@app.route("/")
def hello():
    db = None
    try:
        db = mysql.connector.connect(
            user=os.getenv("DB_USER"),
            host=os.getenv("DB_HOST"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_DATABASE")
        )

        with db.cursor() as cursor:
            cursor.execute("SELECT 'Hello from Flask and MySQL!'")
            result = cursor.fetchone()

        return result[0]
    except mysql.connector.Error as err:
        return f"Error: {err}"
    finally:
        if db and db.is_connected():
            db.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)