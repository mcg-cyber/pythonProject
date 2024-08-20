def greet(name):
    return f'Hello, {name}!'

if __name__ == '__main__':
    ask_user_name = input('What is your name? ')
    print(greet(ask_user_name))