def main():
    # Create a set to store unique names
    names = set()
    while True:
        # Ask the user to enter a name
        name = input("Enter a name (or press Enter to finish): ").strip()
        # Check if the input is an empty string
        if name == "":
            break
        # Check if the name is new or existing
        if name in names:
            print("Existing name")
        else:
            print("New name")
            names.add(name)  # Add the new name to the set
    # Print out the names one by one
    print("\nList of names entered:")
    for name in names:
        print(name)


# Run the main function
if __name__ == "__main__":
    main()
