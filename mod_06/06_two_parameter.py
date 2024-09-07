import math

def calculate_price_per_square_centimeter(diameter, price):
    radius = diameter / 2
    area = math.pi * (radius ** 2)  # Area of the pizza
    price_per_sqm = price / area      # Price per square centimeter
    return price_per_sqm

def main():

    # Create a list of tuples, each containing (diameter in cm, price in dollars)
    pizzas = [
        (30, 10.99),  # 30 cm pizza for $10.99
        (25, 8.49),   # 25 cm pizza for $8.49
        (40, 15.99),  # 40 cm pizza for $15.99
        (35, 12.99)   # 35 cm pizza for $12.99
    ]

    # Print headers for the output
    print(f"{'Diameter (cm)':<20} {'Price ($)':<10} {'Price per cm² ($)':<20}")

    # Iterate over the list and calculate price per square centimeter for each pizza
    for diameter, price in pizzas:
        price_per_cm2 = calculate_price_per_square_centimeter(diameter, price)
        print(f"{diameter:<20} {price:<10} {price_per_cm2:<20.4f}")

if __name__ == "__main__":
    main()
