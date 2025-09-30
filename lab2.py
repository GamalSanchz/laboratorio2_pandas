# primero importamos las librerías necesarias
import pandas as pd
import numpy as np
from pathlib import Path
import sys
# Definimos la ruta al archivo CSV (ajustar según sea necesario)
RUTA = Path(__file__).resolve().parent / "data" / "world_economics.csv"
# Función para imprimir una línea divisoria
def linea():
    print("-" * 90)
# Función principal
def main():
    if not RUTA.exists():
        print(f"No encuentro el archivo CSV en: {RUTA}")
        sys.exit(1)
# Cargar el dataset
    df = pd.read_csv(RUTA)
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 140)

    # numeral 1 (intro)
    print("1. Seleccione un dataset propio (CSV) utilizando la página de https://www.kaggle.com/ y descárguelo para su uso.")
    print(f"   → Archivo usado: {RUTA}")
    linea()

    # numeral 2 (describe)
    print("2. Usar describe() de la librería Pandas para resumir la información del dataset.")
    print(df.describe(include="all").round(2))
    linea()

    # numeral 3 (dtypes)
    print("3. Identificar los tipos de datos de cada columna utilizando dtypes y qué tipo de análisis se puede hacer sobre esta información.")
    print(df.dtypes.astype(str))
    linea()

    # numeral 4 (head y tail)
    print("4. Mostrar los primeros y últimos registros (head(), tail()) para detectar tendencias.")
    print("\n   head() (primeras 5 filas):")
    print(df.head().to_string(index=False))
    print("\n   tail() (últimas 5 filas):")
    print(df.tail().to_string(index=False))
    linea()

    # numeral 5
    print("5. Ordenar los resultados (sort_values()) para ver cuáles categorías destacan más o menos.")
    # Elige automáticamente una columna numérica razonable (por lo general GDP o Population)
    prioridad = ["GDP", "Population", "Debt/GDP", "Inflation Rate", "GDP Growth"]
    num_cols = [c for c in prioridad if c in df.columns and pd.api.types.is_numeric_dtype(df[c])]
    if not num_cols:
        num_cols = df.select_dtypes(include="number").columns.tolist()
    if num_cols:
        col_orden = num_cols[0]
        print(f"   → Ordenado por '{col_orden}' (descendente), top 10:")
        cols_show = ["name", col_orden] if "name" in df.columns else [col_orden]
        print(df[cols_show].sort_values(col_orden, ascending=False).head(10).round(2).to_string(index=False))
    else:
        print("   (No hay columnas numéricas para ordenar).")
    linea()

    # numeral 6 (medidas estadísticas)
    print("6. Seleccionar una columna y, calcular al menos dos de las siguientes medidas:")
    print("   a. Media (np.mean())")
    print("   b. Mediana (np.median())")
    print("   c. Desviación estándar (np.std())")

    # Columna elegida para las medidas (mismo criterio que arriba)
    if not num_cols:
        print("   (No hay columnas numéricas para calcular medidas).")
        return
    col = num_cols[0]
    serie = df[col].dropna().to_numpy()
    #calculo de la media
    media = float(np.mean(serie))
    #calculo de la mediana
    mediana = float(np.median(serie))
    # calculo de la desviación estándar
    desv = float(np.std(serie, ddof=0))  

# Resultados
    print(f"\n   → Columna seleccionada: {col}")
    print(f"   a) Media: {media:.4f}")
    print(f"   b) Mediana: {mediana:.4f}")
    print(f"   c) Desviación estándar: {desv:.4f}")
# Fin del reporte
    linea()
    print("\n✔ Fin del reporte. (Todo mostrado en consola)")

if __name__ == "__main__":
    main()
