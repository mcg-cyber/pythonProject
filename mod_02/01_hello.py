# Script asks user's name then greets the user

def greet(name):
    return f'Terve, {name}!'

if __name__ == '__main__':
    ask_user_name = input('What is your name? ')
    print(greet(ask_user_name))
