import pandas as pd


def transform_weather_data(raw_data):

    hourly = raw_data["hourly"]

    df = pd.DataFrame({
        "datetime": hourly["time"],
        "temperature": hourly["temperature_2m"],
        "humidity": hourly["relative_humidity_2m"],
        "precipitation": hourly["precipitation"]
    })

    df["datetime"] = pd.to_datetime(df["datetime"])

    df = df.drop_duplicates(subset=["datetime"])

    df = df.dropna()

    df = df.sort_values("datetime")

    return df