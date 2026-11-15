# analizar_datos.py
# Script para explorar el archivo "datos_economicos_latam.csv"
# Requisito: tener pandas instalado (pip install pandas)

import pandas as pd

# 1. Leer el archivo CSV y guardarlo en una tabla (DataFrame) llamada "df"
#    El archivo debe estar en la misma carpeta que este script.
df = pd.read_csv("datos_economicos_latam.csv")

# 2. Mostrar las primeras 5 filas para tener una idea de cómo son los datos
print("=" * 60)
print("1) PRIMERAS 5 FILAS")
print("=" * 60)
print(df.head())

# 3. Mostrar cuántas filas y columnas tiene la tabla
#    df.shape devuelve una pareja: (número de filas, número de columnas)
filas, columnas = df.shape
print("\n" + "=" * 60)
print("2) TAMAÑO DE LA TABLA")
print("=" * 60)
print(f"Filas: {filas}")
print(f"Columnas: {columnas}")

# 4. Mostrar el nombre de cada columna y su tipo de dato
print("\n" + "=" * 60)
print("3) COLUMNAS Y TIPOS DE DATOS")
print("=" * 60)
print(df.dtypes)

# 5. Contar cuántos registros hay por país y por indicador
print("\n" + "=" * 60)
print("4) REGISTROS POR PAÍS")
print("=" * 60)
print(df["country"].value_counts())

print("\n" + "=" * 60)
print("5) REGISTROS POR INDICADOR")
print("=" * 60)
print(df["indicator"].value_counts())

# 6. Calcular el rango de años disponibles
#    Convertimos la columna "date" a fecha; si algún valor no se puede
#    convertir, queda como vacío (NaT) y se ignora en el cálculo.

print("\n" + "=" * 60)
print("6) RANGO DE AÑOS")
print("=" * 60)
print("Año mínimo:", df['date'].min())
print("Año máximo:", df['date'].max())
   


# 7. Revisar si hay valores vacíos (nulos) en cada columna
print("\n" + "=" * 60)
print("7) VALORES VACÍOS POR COLUMNA")
print("=" * 60)
vacios = df.isnull().sum()
print(vacios)

if vacios.sum() == 0:
    print("\nNo hay valores vacíos en el archivo.")
else:
    print(f"\nHay {vacios.sum()} valores vacíos en total.")