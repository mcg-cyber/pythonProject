import requests

def get_weather_data(municipality_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={municipality_name}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature_kelvin = data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15

        return weather_description, temperature_celsius
    else:
        return None, None

def main():
    municipality_name = input("Enter the name of the municipality: ")
    api_key = "YOUR_API_KEY"  # Replace 'YOUR_API_KEY' with your actual API key

    weather_description, temperature_celsius = get_weather_data(municipality_name, api_key)

    if weather_description and temperature_celsius:
        print(f"Weather in {municipality_name}: {weather_description}")
        print(f"Temperature: {temperature_celsius}°C")
    else:
        print("Failed to retrieve weather information. Please check the municipality name and API key.")

if __name__ == "__main__":
    main()
