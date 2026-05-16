import requests

# Your API Key
API_KEY = "22a800370abeb7abd8ddf479301158bd"

print("=" * 40)
print("        WEATHER APP")
print("=" * 40)

# User Input
city = input("\nEnter city name: ").strip()

# Check empty input
if city == "":
    print("❌ Please enter a city name.")

else:
    # API URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        # Request Data
        response = requests.get(url)

        # Convert response to JSON
        data = response.json()

        # Check if city exists
        if response.status_code == 200:

            # Extract weather information
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather = data["weather"][0]["description"]
            country = data["sys"]["country"]

            # Display Output
            print("\n🌍 Location:", city.title() + ",", country)
            print(f"🌡️ Temperature: {temperature}°C")
            print(f"💧 Humidity: {humidity}%")
            print(f"☁️ Condition: {weather.title()}")

        else:
            print("❌ City not found.")

    except requests.exceptions.RequestException:
        print("❌ Internet connection error.")
