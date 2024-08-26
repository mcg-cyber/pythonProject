# Purpose: This scripts finds the smallest and largest number entered by user
# License: MIT
# Todo: Add exception handling

numbers = [] # empty list. List is mutable!

while True: # conditional boolean. True/False built-in keyword
    num_input = input("Enter a number (or press Enter to quit): ") # user input

    if num_input == "": # if condition, when no input enetered then program exists
        break # with break built-in keyword


    number = float(num_input) # variables assigned to num_inout as float type
    numbers.append(number) # appends user input (number) to numbers list

if numbers: # does exsists, has numbers in it then
    smallest = min(numbers) # finds the min number in the numbers list (min) keyword
    largest = max(numbers) # finds the max number in the numers list (max) keyword

    print(f"The smallest number is: {smallest}") # prints the result
    print(f"The largest number is: {largest}") # prints the result
    # print(f"Just checking the numbers in the numbers list \n {numbers}")
else:
    print("No numbers entered.") # in case entered something else than a digit
