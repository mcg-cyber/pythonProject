__author__ = '<Cahit Gunes>'
__email__ = '<cahit.gunes@metropolia.fi>'
# Script calculates the area of circle with given size
from math import pi

def circle_area(radius):
    return pi * (radius ** 2)

if __name__ == '__main__':
    radius = float(input("Enter the radius of the circle: "))
    area = circle_area(radius)
    print(f"The area of the circle is: {area}")

