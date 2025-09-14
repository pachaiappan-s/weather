import requests

def get_weather(location, api_key):
    base_url = " https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,          
        "appid":api_key ,       
        "units": "metric"       
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises HTTPError for bad responses

        data = response.json()

        city = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]

        print("\n--- Current Weather ---")
        print(f"Location: {city}, {country}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition.capitalize()}")
        print("-----------------------")

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
    except KeyError:
        print("Could not retrieve weather data. Please check your location.")

if __name__ == "__main__":
    api_key = "0ba26bef67673ba8af57bbc9f42ce8a4"  # Replace with your OpenWeatherMap API key
    location = input("Enter city name or ZIP code: ").strip()
    get_weather(location, api_key)
