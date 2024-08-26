# This script converts inches to centimeters, after calculation ends the program

while True:
    inchesInFloat = float(input("Enter number in inches: "))

    if inchesInFloat < 0:
	#print("Negative number is entered. Exiting ...")
        break

    inches = 2.54
    print(f"{inchesInFloat} inches is equal to centimeters {inches * inchesInFloat}")
    break # exits after calculation (optinal)
