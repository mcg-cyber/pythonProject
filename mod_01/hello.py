__author__ = '<Cahit Gunes>'
__email__ = '<cahit.gunes@metrolpolia.fi>'

def greet(name):
    return f'Hei, {name}!'

if __name__ == '__main__':
    ask_user_name = input('What is your name? ')
    print(greet(ask_user_name))