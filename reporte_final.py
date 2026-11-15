# reporte_final.py
# Genera el archivo "reporte_economico.xlsx" con tres hojas: Resumen, Datos y Notas
# Requisitos: pandas y openpyxl
# Si te falta alguno, se instalan con: pip install pandas openpyxl

import pandas as pd
from openpyxl.styles import Font, Alignment, PatternFill

# 1. Leer el CSV (debe estar en la misma carpeta que este script)
#    La columna "date" es el año como número entero, así que no se convierte
df = pd.read_csv("datos_economicos_latam.csv")

# 2. Quitar la columna "unit" y traducir los códigos de indicador a nombres legibles
df = df.drop(columns=["unit"])

nombres = {
    "NY.GDP.MKTP.KD.ZG": "Crecimiento PIB",
    "FP.CPI.TOTL.ZG": "Inflación",
    "SL.UEM.TOTL.ZS": "Desempleo",
}
# Si apareciera un código desconocido, se conserva tal cual para no perder datos
df["indicador"] = df["indicator"].map(nombres).fillna(df["indicator"])

# 3. Preparar la hoja "Resumen": promedio, mínimo y máximo entre 2010 y 2024
df_periodo = df[(df["date"] >= 2010) & (df["date"] <= 2024)]

resumen = (
    df_periodo.groupby(["country", "indicador"])["value"]
    .agg(["mean", "min", "max"])
    .round(2)
    .reset_index()
    .sort_values(["country", "indicador"])
)
resumen.columns = ["País", "Indicador", "Promedio", "Mínimo", "Máximo"]

# 4. Preparar la hoja "Datos": datos completos, ordenados por país, indicador y año
datos = (
    df[["country", "indicador", "date", "value"]]
    .sort_values(["country", "indicador", "date"])
)
datos.columns = ["País", "Indicador", "Año", "Valor"]

# 5. Preparar la hoja "Notas": un texto por fila
anio_min = int(df["date"].min())
anio_max = int(df["date"].max())

lineas_notas = [
    "FUENTE DE LOS DATOS",
    "Banco Mundial, World Development Indicators (WDI).",
    "",
    "AÑOS CUBIERTOS",
    f"La hoja 'Datos' incluye todos los años disponibles: de {anio_min} a {anio_max}.",
    "La hoja 'Resumen' calcula promedio, mínimo y máximo solo entre 2010 y 2024.",
    "",
    "SIGNIFICADO DE CADA INDICADOR",
    "Crecimiento PIB: cuánto creció (o se redujo, si es negativo) la economía del país "
    "respecto al año anterior, en porcentaje. Un valor de 3 significa que la economía creció un 3 %.",
    "Inflación: cuánto subieron en promedio los precios de bienes y servicios respecto al año "
    "anterior, en porcentaje. Un valor de 5 significa que todo costó, en promedio, un 5 % más.",
    "Desempleo: porcentaje de personas que quieren trabajar y buscan empleo, pero no lo "
    "encuentran, sobre el total de la fuerza laboral.",
]
notas = pd.DataFrame({"Notas": lineas_notas})

# 6. Escribir las tres hojas en el archivo Excel
archivo = "reporte_economico.xlsx"

with pd.ExcelWriter(archivo, engine="openpyxl") as escritor:
    resumen.to_excel(escritor, sheet_name="Resumen", index=False)
    datos.to_excel(escritor, sheet_name="Datos", index=False)
    notas.to_excel(escritor, sheet_name="Notas", index=False)

    # 7. Dar formato: encabezados en negrita, filas fijas arriba y columnas con buen ancho
    for hoja in escritor.book.worksheets:
        hoja.freeze_panes = "A2"  # el encabezado queda fijo al desplazarse

        # Encabezados: negrita, texto blanco, fondo azul oscuro y texto centrado
        for celda in hoja[1]:
            celda.font = Font(bold=True, color="FFFFFF")
            celda.fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
            celda.alignment = Alignment(horizontal="center", vertical="center")

        if hoja.title == "Notas":
            # Columna ancha y con ajuste de texto para que se lea completa
            hoja.column_dimensions["A"].width = 100
            for fila in hoja.iter_rows(min_row=2):
                for celda in fila:
                    celda.alignment = Alignment(wrap_text=True, vertical="top")
                    # Los títulos de sección (en mayúsculas) van en negrita,
                    # con letra azul oscuro y un fondo azul claro
                    if celda.value and celda.value.isupper():
                        celda.font = Font(bold=True, color="1F4E78")
                        celda.fill = PatternFill(start_color="DDEBF7", end_color="DDEBF7", fill_type="solid")
        else:
            # Ajustar el ancho de cada columna al texto más largo que contiene
            for columna in hoja.columns:
                ancho = max(len(str(celda.value or "")) for celda in columna) + 2
                hoja.column_dimensions[columna[0].column_letter].width = ancho

print(f"Archivo creado: {archivo}")