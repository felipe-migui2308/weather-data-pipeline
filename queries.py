import sqlite3

conn = sqlite3.connect("data/weather.db")

cursor = conn.cursor()

# CONSULTA 1 - Total de registros
print("\n=== TOTAL DE REGISTROS ===")

cursor.execute("""
    SELECT COUNT(*)
    FROM weather
""")

print(cursor.fetchone()[0])


# CONSULTA 2 - Temperatura média
print("\n=== TEMPERATURA MÉDIA ===")

cursor.execute("""
    SELECT ROUND(AVG(temperature), 2)
    FROM weather
""")

print(cursor.fetchone()[0], "°C")


# CONSULTA 3 - Temperaturas por dia
print("\n=== TEMPERATURAS POR DIA ===")

cursor.execute("""
    SELECT
        DATE(datetime) AS dia,
        ROUND(AVG(temperature), 2) AS media,
        MAX(temperature) AS maxima,
        MIN(temperature) AS minima
    FROM weather
    GROUP BY DATE(datetime)
    ORDER BY dia
""")

for row in cursor.fetchall():
    print(row)


# CONSULTA 4 - Dias com precipitação
print("\n=== PRECIPITAÇÃO POR DIA ===")

cursor.execute("""
    SELECT
        DATE(datetime) AS dia,
        ROUND(SUM(precipitation), 2) AS total_mm
    FROM weather
    GROUP BY DATE(datetime)
    ORDER BY total_mm DESC
""")

for row in cursor.fetchall():
    print(row)


conn.close()