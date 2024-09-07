def filter_positive_numbers(numbers):
    return [num for num in numbers if num > 0] # compherension 
    """
    for num in numbers:
       if num > 0
    return num
    """

def main():

    test_list = [1, -2, 3, 0, -5, 10, -1] 

    # Calling the function and getting the filtered list
    positive_numbers = filter_positive_numbers(test_list)

    # Printing out the value
    print(f"The original list: {test_list}")
    print(f"The filtered list of positive numbers: {positive_numbers}")

if __name__ == "__main__":
    main()
