def gallons_to_liters(gallons):
    liters_per_gallon = 3.78541  # 1 gallon is approximately 3.78541 liters
    return gallons * liters_per_gallon

def main():
    gallons = float(input("Enter the quantity of gasoline in gallons: "))

    liters = gallons_to_liters(gallons)

    print(f"{gallons} gallons is equal to {liters:.2f} liters.")

if __name__ == "__main__":
    main()
