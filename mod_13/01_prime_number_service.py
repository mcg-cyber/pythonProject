#readme = """ 
#http://127.0.0.1:5000/prime_number/31
#pip install Flask 
#"""

from flask import Flask, jsonify

app = Flask(__name__)

def is_prime_number(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

@app.route('/prime_number/<int:num>', methods=['GET'])
def check_prime_number(num):
    is_prime = is_prime_number(num)
    response = {
        "Number": num,
        "isPrime": is_prime
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
