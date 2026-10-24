import urllib.request
import urllib.parse
import json

def get_weather(city_name):
    """
    Fetches real-time weather details without requiring an API key.
    """
    # wttr.in provides JSON formatted weather data publicly
    encoded_city = urllib.parse.quote(city_name)
    url = f"https://wttr.in/{encoded_city}?format=j1"

    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())

            current = data["current_condition"][0]
            temp_c = current["temp_C"]
            feels_like_c = current["FeelsLikeC"]
            humidity = current["humidity"]
            pressure = current["pressure"]
            description = current["weatherDesc"][0]["value"]
            wind_speed = current["windspeedKmph"]

            print("\n" + "=" * 45)
            print(f" Weather Report: {city_name.title()}")
            print("=" * 45)
            print(f" Condition   : {description}")
            print(f" Temperature : {temp_c} °C (Feels like: {feels_like_c} °C)")
            print(f" Humidity    : {humidity}%")
            print(f" Pressure    : {pressure} hPa")
            print(f" Wind Speed  : {wind_speed} km/h")
            print("=" * 45 + "\n")

    except urllib.error.HTTPError as e:
        print(f"\n[Error] Unable to fetch data (HTTP {e.code})\n")
    except urllib.error.URLError:
        print("\n[Error] Network error. Check your internet connection.\n")
    except (KeyError, IndexError):
        print("\n[Error] City not found or format unexpected.\n")

def main():
    print("=" * 45)
    print("      Basic Weather Application (OIBSIP)     ")
    print("=" * 45)

    while True:
        city = input("Enter city name (or type 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("Exiting application. Goodbye!")
            break
        if not city:
            print("Please enter a valid city name.")
            continue

        get_weather(city)

if __name__ == "__main__":
    main()