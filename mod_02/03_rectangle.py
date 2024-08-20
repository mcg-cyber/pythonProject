__author__ = '<Cahit Gunes>'
__email__ = '<cahit.gunes@metropolia.fi>'
# Script calculates the area of rectangle with given sizes

def rectangle(b, h):
    return b * h

if __name__ == '__main__':
    base = int(input("Enter the base: "))
    height = int(input("Enter the height: "))
    print(rectangle(base, height))