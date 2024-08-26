# This script checks whether the fish can be catch or not

fish_size = 42
print("Enter the (fish) Zander size: ")
size = float(input())

if size >= fish_size:
    print("The fish is catch")
else:
    print(f"The fish is not catch. Fish (Zander) size must be {fish_size} cm")
    print("Please return the fish back to the river")
