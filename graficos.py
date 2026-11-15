# graficos_indicadores.py
# Genera dos gráficos a partir de "datos_economicos_latam.csv"
# Requisitos: pandas y matplotlib
# Si matplotlib no está instalado, se instala con: pip install matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV (debe estar en la misma carpeta que este script)
# La columna "date" es el año como número entero, así que no la convertimos
df = pd.read_csv("datos_economicos_latam.csv")

# ---------------------------------------------------------------
# GRÁFICO 1: evolución del crecimiento del PIB por país (líneas)
# ---------------------------------------------------------------

# Nos quedamos solo con el indicador de crecimiento del PIB y sin valores vacíos
pib = df[df["indicator"] == "NY.GDP.MKTP.KD.ZG"].dropna(subset=["value"])

# Crear la figura (tamaño en pulgadas: ancho, alto)
plt.figure(figsize=(11, 6))

# Dibujar una línea por país, ordenando los datos por año
for pais, datos in pib.groupby("country"):
    datos = datos.sort_values("date")
    plt.plot(datos["date"], datos["value"], marker="o", markersize=4, label=pais)

# Línea horizontal en 0 para distinguir crecimiento de contracción
plt.axhline(0, color="gray", linewidth=0.8, linestyle="--")

# Títulos, etiquetas de los ejes y leyenda
plt.title("Evolución del crecimiento del PIB en América Latina", fontsize=14)
plt.xlabel("Año")
plt.ylabel("Crecimiento del PIB (% anual)")
plt.legend(title="País")
plt.grid(alpha=0.3)

# Guardar el gráfico como imagen PNG
plt.tight_layout()
plt.savefig("crecimiento_pib.png", dpi=150)
plt.close()
print("Gráfico guardado: crecimiento_pib.png")

# ---------------------------------------------------------------
# GRÁFICO 2: inflación de cada país en 2024 (barras, de mayor a menor)
# ---------------------------------------------------------------

# Filtrar la inflación del año 2024 y ordenar de mayor a menor
inflacion = df[(df["indicator"] == "FP.CPI.TOTL.ZG") & (df["date"] == 2024)]
inflacion = inflacion.dropna(subset=["value"]).sort_values("value", ascending=False)

if inflacion.empty:
    print("No hay datos de inflación para 2024, no se creó el segundo gráfico.")
else:
    plt.figure(figsize=(10, 6))

    # Dibujar las barras (una por país)
    barras = plt.bar(inflacion["country"], inflacion["value"], color="steelblue")

    # Mostrar el valor encima de cada barra
    plt.bar_label(barras, fmt="%.1f%%", padding=3)

    # Títulos y etiquetas; los nombres de países se inclinan para que se lean bien
    plt.title("Inflación en América Latina, 2024", fontsize=14)
    plt.xlabel("País")
    plt.ylabel("Inflación (% anual)")
    plt.xticks(rotation=30, ha="right")
    plt.grid(axis="y", alpha=0.3)

    # Guardar el gráfico como imagen PNG
    plt.tight_layout()
    plt.savefig("inflacion_2024.png", dpi=150)
    plt.close()
    print("Gráfico guardado: inflacion_2024.png")