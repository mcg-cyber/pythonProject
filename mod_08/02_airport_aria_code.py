# FIX: fetchs from flight_game, airport table
# SELECT airport.name, airport.type FROM airport WHERE ident = "EFHK" ORDER BY airport.type;
# With "FI", returns empty set with script and mariadb command above
# FIX is done with this SQL code below sorts better now

#SELECT airport.type, count(*)
#       FROM airport
#       WHERE iso_country = %s
#       GROUP BY airport.type
#       ORDER BY count(*) DESC


# SQL command below works also

#cursor = connection.cursor()
    #   cursor.execute(
    #       """
    #       SELECT airport.name, airport.type
    #       FROM airport
    #       WHERE iso_country = %s
    #       ORDER BY airport.type
    #   """,
    #       (area_code,),
    #   )


import mysql.connector
from mysql.connector import Error


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


def fetch_airports_by_area_code(connection, area_code):
    """Fetch airports located in the specified area code ordered by airport type"""
    cursor = connection.cursor()
    #   cursor.execute(
    #       """
    #       SELECT airport.name, airport.type
    #       FROM airport
    #       WHERE iso_country = %s
    #       ORDER BY airport.type
    #   """,
    #       (area_code,),
    #   )
    cursor.execute(
        """
       SELECT airport.type, count(*)
       FROM airport
       WHERE iso_country = %s
       GROUP BY airport.type
       ORDER BY count(*) DESC
    """,
        (area_code,),
    )
    results = cursor.fetchall()
    cursor.close()
    return results


def main():
    # Create a database connection
    connection = create_connection()
    if connection is None:
        return
    area_code = input("Enter the area code (e.g., 'FI' for Finland): ").strip().upper()
    airports = fetch_airports_by_area_code(connection, area_code)
    if airports:
        print(f"\nAirports in country with area code '{area_code}':")
        for airport_name, airport_type in airports:
            print(f"{airport_name} - {airport_type}")
    else:
        print(f"No airports found for area code '{area_code}'.")
    # Close the database connection
    connection.close()


# Run the main function
if __name__ == "__main__":
    main()
