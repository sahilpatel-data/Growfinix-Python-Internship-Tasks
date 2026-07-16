import requests
import json

# ==========================
# ERROR HANDLING
# ==========================

try:
    # Get city name
    city = input("Enter city name: ")

    # --------------------------
    # GET LATITUDE & LONGITUDE
    # --------------------------

    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

    response = requests.get(url, timeout=10)

    data = response.json()

    if "results" not in data:
        print("City not found.")
        exit()

    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]

    print("\nCity:", city)
    print("Latitude:", latitude)
    print("Longitude:", longitude)

    # ==========================
    # GET CURRENT WEATHER
    # ==========================

    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        "&current=temperature_2m,wind_speed_10m,weather_code"
    )

    weather_response = requests.get(weather_url, timeout=10)

    weather_data = weather_response.json()

    current = weather_data["current"]

    temperature = current["temperature_2m"]
    wind_speed = current["wind_speed_10m"]
    weather_code = current["weather_code"]

    print("\n===== CURRENT WEATHER =====")
    print(f"City: {city}")
    print(f"Temperature: {temperature} °C")
    print(f"Wind Speed: {wind_speed} km/h")

    # ==========================
    # WEATHER DESCRIPTION
    # ==========================

    weather_codes = {
        0: "Clear Sky",
        1: "Mainly Clear",
        2: "Partly Cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing Rime Fog",
        51: "Light Drizzle",
        53: "Moderate Drizzle",
        55: "Dense Drizzle",
        61: "Light Rain",
        63: "Moderate Rain",
        65: "Heavy Rain",
        71: "Light Snow",
        73: "Moderate Snow",
        75: "Heavy Snow",
        80: "Rain Showers",
        81: "Moderate Rain Showers",
        82: "Violent Rain Showers",
        95: "Thunderstorm"
    }

    weather_description = weather_codes.get(
        weather_code,
        "Unknown Weather"
    )

    print(f"Weather: {weather_description}")
    print(f"Weather Code: {weather_code}")

    print("\n===== WEATHER SUMMARY =====")
    print(f"City: {city}")
    print(f"Temperature: {temperature} °C")
    print(f"Wind Speed: {wind_speed} km/h")
    print(f"Condition: {weather_description}")

    # ==========================
    # SAVE JSON RESPONSE
    # ==========================

    with open(
        "responses/weather_response.json",
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            weather_data,
            file,
            indent=4
        )

    print("\nWeather API response saved to responses/weather_response.json")

# ==========================
# EXCEPTION HANDLING
# ==========================

except requests.exceptions.ConnectionError:
    print("Error: Unable to connect to the internet. Please check your connection.")

except requests.exceptions.Timeout:
    print("Error: The request timed out. Please try again later.")

except requests.exceptions.RequestException as e:
    print(f"Request Error: {e}")

except Exception as e:
    print(f"Unexpected Error: {e}")

# ==========================
# GENERATE WEATHER REPORT
# ==========================

report = f"""
========================================
        WEATHER REPORT
========================================

City            : {city}

Latitude        : {latitude}
Longitude       : {longitude}

Temperature     : {temperature} °C

Wind Speed      : {wind_speed} km/h

Condition       : {weather_description}

Weather Code    : {weather_code}

========================================
Generated Successfully
========================================
"""

print(report)

with open(
    "responses/weather_report.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(report)

print("Weather report saved to responses/weather_report.txt")