import requests

def fetch_random_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        joke_data = response.json()
        joke_text = joke_data['value']
        return joke_text
    else:
        return "Failed to fetch Chuck Norris joke"

random_joke = fetch_random_joke()
print(random_joke)
