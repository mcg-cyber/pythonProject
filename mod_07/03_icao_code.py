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
            autocommit=True,
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


def fetch_airport_info(connection, icao_code):
    """Fetch airport information from the database"""
    # sql_command = f"select * from airport where ident = %s"
    # print(sql_command, (icao_code,))
    cursor = connection.cursor(dictionary=True)
    # cursor.execute(sql_command, (icao_code,))
    # cursor = connection.cursor()
    cursor.execute("SELECT * FROM airport WHERE ident = %s", (icao_code,))
    result = cursor.fetchone()
    cursor.close()
    # return result[0] if result else None
    return result


def main():
    # Create a database connection
    connection = create_connection()
    if connection is None:
        return
    while True:
        # options to the user
        print("\nOptions:")
        print("1. Enter a new airport")
        print("2. Fetch airport information")
        print("3. Quit")

        choice = input("Please choose an option (1, 2, or 3): ").strip()
        if choice == "1":
            # Enter a new airport
            icao_code = input("Enter the ICAO code of the airport: ").strip().upper()
            airport_name = input("Enter the name of the airport: ").strip()
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO airport (ident, airport.name) VALUES (%s, %s)",
                (icao_code, airport_name),
            )
            connection.commit()
            cursor.close()
            print(
                f"Airport '{airport_name}' with ICAO code '{icao_code}' has been added."
            )
        elif choice == "2":
            # Fetch airport information
            icao_code = (
                input("Enter the ICAO code of the airport to fetch information: ")
                .strip()
                .upper()
            )
            airport_name = fetch_airport_info(connection, icao_code)
            if airport_name:
                print(f"The airport with ICAO code '{icao_code}' is '{airport_name}'.")
            else:
                print(f"No airport found with ICAO code '{icao_code}'.")
        elif choice == "3":
            # Quit the program
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")
    # Close the database connection
    connection.close()


# Run the main function
if __name__ == "__main__":
    main()
