__author__ = '<Cahit Gunes>'
__email__ = '<cahit.gunes@metropolia.fi>'
__version__ = '0.0.1'

def greet(name):
    return f'Hello, {name}!'

if __name__ == '__main__':
    ask_user_name = input('What is your name? ')
    print(greet(ask_user_name))