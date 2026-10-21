from src.extract import extract_weather_data
from src.transform import transform_weather_data
from src.load import load_weather_data


def main():

    print("Iniciando pipeline ETL...")

    print("Extraindo dados...")
    raw_data = extract_weather_data()

    print("Transformando dados...")
    df = transform_weather_data(raw_data)

    print(f"Registros processados: {len(df)}")

    print("Carregando dados no SQLite...")
    load_weather_data(df)

    print("Pipeline executado com sucesso!")


if __name__ == "__main__":
    main()