import requests


def extract_weather_data():

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": -19.9167,
        "longitude": -43.9345,
        "hourly": [
            "temperature_2m",
            "relative_humidity_2m",
            "precipitation"
        ],
        "forecast_days": 3,
        "timezone": "America/Sao_Paulo"
    }

    response = requests.get(
        url,
        params=params,
        timeout=30
    )

    response.raise_for_status()

    return response.json()