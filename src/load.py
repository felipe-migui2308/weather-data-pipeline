import sqlite3
from pathlib import Path


DATABASE_PATH = Path("data/weather.db")


def load_weather_data(df):

    DATABASE_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with sqlite3.connect(DATABASE_PATH) as conn:

        conn.execute("""
            CREATE TABLE IF NOT EXISTS weather (
                datetime TEXT PRIMARY KEY,
                temperature REAL,
                humidity REAL,
                precipitation REAL
            )
        """)

        records = [
            (
                row.datetime.isoformat(),
                float(row.temperature),
                float(row.humidity),
                float(row.precipitation)
            )
            for row in df.itertuples(index=False)
        ]

        conn.executemany("""
            INSERT INTO weather (
                datetime,
                temperature,
                humidity,
                precipitation
            )
            VALUES (?, ?, ?, ?)
            ON CONFLICT(datetime) DO UPDATE SET
                temperature = excluded.temperature,
                humidity = excluded.humidity,
                precipitation = excluded.precipitation
        """, records)

        conn.commit()