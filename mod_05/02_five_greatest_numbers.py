# This script sorts the five greatest numbers entered by user

numbers = [] # empty list

while True:
    user_input = input("Enter a number (or press Enter to quit): ") # user prompt for numbers

    if user_input == "": # if user enters empty input then quits
        break # consider using sys.exit()
    
    numbers.append(user_input) # appending user_input to the numbers list

    sorted_numbers = sorted(numbers, reverse=True) # sorting by reversing
    top_five = sorted_numbers[:5] # slicing numbers list from begining until 5 

    print("\nThe five greatest numbers are (in descending order):")
    for i, j in enumerate(top_five, start=1): # using enumerate built-in function to index iterable
        print(f"{i}-> {j}")
else:
    print("No numbers were entered.")
