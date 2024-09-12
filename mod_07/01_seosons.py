def get_season(month):
    # Define the seasons in a tuple
    seasons = ("Winter", "Spring", "Summer", "Aut")

    # Determine the season based on the month
    if month in [12, 1, 2]:
        return seasons[0]  # Winter
    elif month in [3, 4, 5]:
        return seasons[1]  # Spring
    elif month in [6, 7, 8]:
        return seasons[2]  # Summer
    elif month in [9, 10, 11]:
        return seasons[3]  # Autumn
    else:
        return None  # Invalid month


# Ask the user for a month number
try:
    month_number = int(input("Enter a month number (1-12): "))
    season = get_season(month_number)

    if season:
        print(f"The corresponding season is: {season}")
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")
except ValueError:
    print("Please enter a valid integer.")
