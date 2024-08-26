# This script returns to the passanger seat type then guides accordingly with the given seat info in input prompt
# by using simple if/else syntax 

print("Ener the name of your seat")
seat_name = str(input()) # built-in input function
# conditional check starts here
if seat_name == "LUX":
    print(" Upper-deck cabin with a balcony.")
elif seat_name == "A":
    print("Above the car deck, equipped with a window")
elif seat_name == "B":
    print("Windowless cabin above the car deck.")
elif seat_name == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class")
