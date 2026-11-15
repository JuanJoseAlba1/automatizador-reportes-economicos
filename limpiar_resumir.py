# analisis_indicadores.py
# Analiza los indicadores económicos de "datos_economicos_latam.csv"
# Requisito: tener pandas instalado (pip install pandas)

import pandas as pd

# 1. Leer el archivo CSV (debe estar en la misma carpeta que este script)
df = pd.read_csv("datos_economicos_latam.csv")

# 2. Eliminar la columna "unit", que está vacía y no nos sirve
df = df.drop(columns=["unit"])

# 3. Crear la columna "indicador" con nombres legibles
#    Cada código del CSV se traduce usando este diccionario
nombres = {
    "NY.GDP.MKTP.KD.ZG": "Crecimiento PIB",
    "FP.CPI.TOTL.ZG": "Inflación",
    "SL.UEM.TOTL.ZS": "Desempleo",
}
df["indicador"] = df["indicator"].map(nombres)

# Aviso por si hubiera códigos que no están en el diccionario
sin_traducir = df["indicador"].isnull().sum()
if sin_traducir > 0:
    print(f"Aviso: {sin_traducir} filas tienen un código de indicador desconocido.\n")

# 4. Calcular promedio, mínimo y máximo para cada país y cada indicador
#    groupby agrupa las filas; agg calcula las tres estadísticas
#    (los valores vacíos se ignoran automáticamente)
resumen = (
    df.groupby(["country", "indicador"])["value"]
    .agg(promedio="mean", minimo="min", maximo="max")
    .round(2)
    .reset_index()
    .sort_values(["country", "indicador"])
)

print("=" * 60)
print("1) PROMEDIO, MÍNIMO Y MÁXIMO POR PAÍS E INDICADOR")
print("=" * 60)
print(resumen.to_string(index=False))

# 5. Mejor y peor año de crecimiento del PIB por país
#    Primero nos quedamos solo con las filas de "Crecimiento PIB" y sin vacíos
pib = df[df["indicador"] == "Crecimiento PIB"].dropna(subset=["value"])

#    idxmax / idxmin devuelven la fila con el valor más alto / más bajo de cada país
mejor = pib.loc[pib.groupby("country")["value"].idxmax()]
peor = pib.loc[pib.groupby("country")["value"].idxmin()]

mejor = mejor[["country", "date", "value"]].rename(
    columns={"date": "mejor_año", "value": "crecimiento"}
)
peor = peor[["country", "date", "value"]].rename(
    columns={"date": "peor_año", "value": "crecimiento"}
)

print("\n" + "=" * 60)
print("2) MEJOR AÑO DE CRECIMIENTO PIB POR PAÍS")
print("=" * 60)
print(mejor.sort_values("country").to_string(index=False))

print("\n" + "=" * 60)
print("3) PEOR AÑO DE CRECIMIENTO PIB POR PAÍS")
print("=" * 60)
print(peor.sort_values("country").to_string(index=False))

# 6. Año con la inflación más alta de cada país
inflacion = df[df["indicador"] == "Inflación"].dropna(subset=["value"])
max_inflacion = inflacion.loc[inflacion.groupby("country")["value"].idxmax()]
max_inflacion = max_inflacion[["country", "date", "value"]].rename(
    columns={"date": "año", "value": "inflacion_maxima"}
)

print("\n" + "=" * 60)
print("4) AÑO DE MAYOR INFLACIÓN POR PAÍS")
print("=" * 60)
print(max_inflacion.sort_values("country").to_string(index=False))