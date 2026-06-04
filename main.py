from fastapi import FastAPI

app = FastAPI()

weather_data = {
    "pune": {
        "temperature": "30°C",
        "condition": "Sunny"
    },
    "mumbai": {
        "temperature": "32°C",
        "condition": "Cloudy"
    },
    "delhi": {
        "temperature": "38°C",
        "condition": "Hot"
    }
}


@app.get("/")
def home():
    return {"message": "Weather App Running"}


@app.get("/weather/{city}")
def get_weather(city: str):
    city = city.lower()

    if city in weather_data:
        return {
            "city": city,
            "weather": weather_data[city]
        }

    return {"error": "City not found"}