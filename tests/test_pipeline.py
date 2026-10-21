import sqlite3

from src.transform import transform_weather_data
from src.load import load_weather_data
import src.load as load_module


def sample_weather_data():
    return {
        "hourly": {
            "time": [
                "2026-10-21T10:00",
                "2026-10-21T11:00",
                "2026-10-21T11:00"
            ],
            "temperature_2m": [25.0, 26.0, 26.0],
            "relative_humidity_2m": [60, 65, 65],
            "precipitation": [0.0, 1.2, 1.2]
        }
    }


def test_transform_columns():
    df = transform_weather_data(sample_weather_data())

    assert list(df.columns) == [
        "datetime",
        "temperature",
        "humidity",
        "precipitation"
    ]


def test_remove_duplicates():
    df = transform_weather_data(sample_weather_data())

    assert len(df) == 2


def test_temperature_values():
    df = transform_weather_data(sample_weather_data())

    assert df["temperature"].mean() == 25.5


def test_load_without_duplicates(tmp_path, monkeypatch):
    test_database = tmp_path / "weather_test.db"

    monkeypatch.setattr(
        load_module,
        "DATABASE_PATH",
        test_database
    )

    df = transform_weather_data(sample_weather_data())

    load_weather_data(df)
    load_weather_data(df)

    with sqlite3.connect(test_database) as conn:
        count = conn.execute(
            "SELECT COUNT(*) FROM weather"
        ).fetchone()[0]

    assert count == 2