# pip install Flask mysql-connector-python
from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Connect to the MariaDB database
db_connection = mysql.connector.connect(
    host="172.17.0.2",
    port="3306",
    user="root",
    password="mypass",
    database="flight_game"
)
cursor = db_connection.cursor()

@app.route('/airport/<icao>', methods=['GET'])
def get_airport_info(icao):
    query = "SELECT * FROM airport WHERE ICAO = %s"
    cursor.execute(query, (icao,))
    airport_data = cursor.fetchone()

    if airport_data:
        response = {
            "ICAO": airport_data[1],  # Assuming ICAO code is in the second column
            "Name": airport_data[2],  # Assuming airport name is in the third column
            "Location": airport_data[3]  # Assuming location is in the fourth column
        }
        return jsonify(response)
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
