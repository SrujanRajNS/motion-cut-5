import requests

def get_weather_data(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Change to 'imperial' for Fahrenheit.
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        return data
    else:
        return None

def display_weather(data):
    if data:
        city_name = data['name']
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']

        print(f"Weather in {city_name}: {weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    else:
        print("City not found or API request failed.")

def main():
    api_key = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key.
    city = input("Enter a city name: ")
    
    weather_data = get_weather_data(api_key, city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
