def sum_of_integers(numbers):
    """Return the sum of a list of integers."""
    return sum(numbers)

def main():
    """Main program to test the sum_of_integers function."""

    # Creating a list of integers for testing
    test_list = [1, 2, 3, 4, 5, 10, -1]  # Example list of integers

    # Calling the function and getting the sum
    total_sum = sum_of_integers(test_list)

    # Printing out the value
    print(f"The sum of the list {test_list} is: {total_sum}")

if __name__ == "__main__":
    main()
