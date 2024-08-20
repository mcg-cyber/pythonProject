__author__ = '<Cahit Gunes>'
__email__ = '<cahit.gunes@metropolia.fi>'

# Script calculates the sum and (multiplies) average from the given three number

def three_number_calculation():
    numbers = []
    num1 = int(input('Type the first number: '))
    num2 = int(input('Type the second number: '))
    num3 = int(input('Type the third number: '))

    numbers.append(num1)
    numbers.append(num2)
    numbers.append(num3)

    sum = num1 + num2 + num3
    mult = num1 * num2 * num3
    average = sum / len(numbers)

    print(f"The sum of the three numbers is: {sum}")
    print(f"The mult of the three numbers is: {mult}")
    print(f"The average of the three numbers is: {average}")


if __name__ == '__main__':
    three_number_calculation()





