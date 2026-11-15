# automatizador-reportes-economicos
# 📊 Automatizador de Reportes Económicos

Script en Python que convierte datos económicos crudos del Banco Mundial en un reporte profesional con resúmenes, gráficos y un archivo Excel — en segundos, no en 40 minutos.

## 🎯 El problema que resuelve

Revisar y resumir datos económicos de varios países a mano (filtrar, calcular promedios, hacer gráficos, armar el Excel) toma **~40 minutos por reporte**. Este proyecto lo reduce a **un comando**:

```
python reporte_final.py
```

## 🗂️ Datos de entrada

- **Fuente:** [Banco Mundial — World Development Indicators](https://data.worldbank.org) (oficial, gratuito)
- **Registros:** 270 filas = 6 países × 3 indicadores × 15 años (2010–2024)
- **Países:** Colombia, México, Perú, Chile, Brasil, España
- **Indicadores:**
  - `NY.GDP.MKTP.KD.ZG` — Crecimiento del PIB (% anual)
  - `FP.CPI.TOTL.ZG` — Inflación (% anual)
  - `SL.UEM.TOTL.ZS` — Desempleo (%)

Archivo: `datos_economicos_latam.csv` (columnas: `indicator, country, date, unit, value`)

## ⚙️ Qué hace el pipeline

| Script | Etapa | Qué hace |
|---|---|---|
| `analizar_datos.py` | 1. Explorar | Lee el CSV y valida integridad: filas, países, indicadores, años, valores vacíos |
| `limpiar_resumir.py` | 2. Limpiar + resumir | Elimina columnas vacías, traduce códigos a nombres legibles, calcula promedio/mín/máx por país e indicador, detecta mejor/peor año de PIB e inflación máxima |
| `graficos.py` | 3. Visualizar | Genera 2 gráficos PNG: evolución del PIB (líneas) e inflación 2024 comparada (barras) |
| `reporte_final.py` | 4. Entregar | Exporta `reporte_economico.xlsx` con 3 hojas: Resumen, Datos limpios y Notas metodológicas |

## 🚀 Cómo ejecutarlo

1. **Clonar el repo** o descargar los archivos.
2. **Requisitos:** Python 3.10+ y las librerías pandas, matplotlib y openpyxl:

```
pip install pandas matplotlib openpyxl
```

3. **Ejecutar el pipeline completo** (desde la carpeta del proyecto):

```
python analizar_datos.py     # 1. Explorar y validar
python limpiar_resumir.py    # 2. Limpiar y resumir
python graficos.py           # 3. Generar gráficos PNG
python reporte_final.py      # 4. Exportar reporte Excel
```

4. **Resultado:** `reporte_economico.xlsx` + `crecimiento_pib.png` + `inflacion_2024.png`

## 📈 Resultados de ejemplo (2010–2024)

- **Mayor crecimiento promedio del PIB:** Perú (3.56%) y Colombia (3.36%)
- **Peor año general:** 2020 (pandemia) — caídas de hasta -10.9%
- **Rebote general:** 2021 fue el mejor año de PIB en 5 de 6 países
- **Inflación más alta reciente:** Chile y Colombia superaron 11% en 2022-2023

## 🛠️ Tecnologías

Python 3.13 · pandas · matplotlib · openpyxl

*Código desarrollado con asistencia de IA (vibe coding): la IA escribe, yo dirijo, verifico y valido cada etapa.*

## 👤 Autor

**Juan José Alba** — Ingeniero de Sistemas | Automatización con IA
Experiencia gerencial · Máster en Organización Industrial

- 💼 LinkedIn: https://www.linkedin.com/in/juan-josé-alba-arango/

