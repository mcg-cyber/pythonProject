import mysql.connector
from mysql.connector import Error
from geopy.distance import great_circle


def create_connection():
    """Create a database connection to the MySQL database"""
    connection = None
    try:
        connection = mysql.connector.connect(
            host="172.17.0.2",  # Change if your MySQL server is on a different host
            user="root",  # Replace with your MySQL username
            password="mypass",  # Replace with your MySQL password
            database="flight_game",  # Replace with your database name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


def fetch_airport_coordinates(connection, icao_code):
    """Fetch the coordinates of the airport based on ICAO code"""
    cursor = connection.cursor()
    cursor.execute(
        "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s", (icao_code,)
    )
    result = cursor.fetchone()
    cursor.close()
    return result  # Returns (latitude, longitude) or None if not found


def main():
    # Create a database connection
    connection = create_connection()
    if connection is None:
        return
    # Get ICAO codes from the user
    icao_code1 = input("Enter the ICAO code of the first airport: ").strip().upper()
    icao_code2 = input("Enter the ICAO code of the second airport: ").strip().upper()
    # Fetch coordinates for both airports
    coords1 = fetch_airport_coordinates(connection, icao_code1)
    coords2 = fetch_airport_coordinates(connection, icao_code2)
    if coords1 and coords2:
        # Calculate the distance
        distance = great_circle(coords1, coords2).kilometers
        print(
            f"The distance between {icao_code1} and {icao_code2} is {distance:.2f} kilometers."
        )
    else:
        if not coords1:
            print(f"No airport found with ICAO code '{icao_code1}'.")
        if not coords2:
            print(f"No airport found with ICAO code '{icao_code2}'.")
    # Close the database connection
    connection.close()


# Run the main function
if __name__ == "__main__":
    main()
