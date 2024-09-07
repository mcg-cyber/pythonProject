# This script lets user enter five city names using for loop end empy list the adds all to the list
# finally prints all cities to terminal

cities = []
for _ in range(5):
    city = input("Enter the name of a city: ")
    cities.append(city)

print("\nList of cities:")
for city in cities:
    print(city)
