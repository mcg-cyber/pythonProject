# This script asks usernamme and pass
count = 0

while count < 5:
    #count = 0
    username = "python"
    password = "rules"
    print("Enter username: ")
    ask_username = input()
    print("Enter password")
    ask_password = input()
    if ask_username != username and ask_password != password:
        count += 1
        print("Access denied!")
    else:
        print("Welcome!")
        break
    
