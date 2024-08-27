"""A simple Flask application for fetching weather data."""

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


@app.route("/")
def index():
    """Render the index page."""
    return render_template("index.html")


@app.route("/weather")
def get_weather():
    """Fetch weather data for a specified city and date."""
    api_key = "YOUR_API_KEY"
    city_name = "CityName"
    date = request.args.get("date")

    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"q={city_name}&appid={api_key}&units=metric&date={date}"
    )

    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        return jsonify(
            {
                "temperature": weather_data["main"]["temp"],
                "condition": weather_data["weather"][0]["description"],
                "humidity": weather_data["main"]["humidity"],
            }
        )
    else:
        return jsonify({"error": "Failed to fetch weather data"}), response.status_code


if __name__ == "__main__":
    app.run(debug=True)
