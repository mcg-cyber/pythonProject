# Script asks user's name then greets the user

"""
greet = input("What is your name? "
print("Hei" + greet)
"""



def greet(name):
    return f'Hei, {name}!'

if __name__ == '__main__':
    ask_user_name = input('What is your name? ')
    print(greet(ask_user_name))
