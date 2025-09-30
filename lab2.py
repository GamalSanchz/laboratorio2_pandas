# lab2.py (solo salida en terminal)
import pandas as pd
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
CSV = ROOT / "data" / "world_economics.csv"

if not CSV.exists():
    print(f"No encontré el CSV en: {CSV}")
    sys.exit(1)

print(f"Usando CSV: {CSV}\n")
df = pd.read_csv(CSV)

# 1) Forma, columnas, primeras/últimas filas
print("=== SHAPE ===")
print(df.shape)  # (filas, columnas)

print("\n=== COLUMNAS ===")
print(list(df.columns))

print("\n=== HEAD (5) ===")
print(df.head())

print("\n=== TAIL (5) ===")
print(df.tail())

# 2) Tipos y nulos
print("\n=== DTYPES ===")
print(df.dtypes)

print("\n=== NULOS POR COLUMNA ===")
print(df.isna().sum())

# 3) Describe (compatible con cualquier versión de pandas)
print("\n=== DESCRIBE NUMÉRICO ===")
print(df.describe())

print("\n=== DESCRIBE CATEGÓRICO ===")
obj_cols = df.select_dtypes(include="object")
if not obj_cols.empty:
    print(obj_cols.describe())
else:
    print("(No hay columnas categóricas)")

# 4) Top 10 por alguna métrica si existe
for col in ["GDP", "Population", "Debt/GDP", "Inflation Rate", "GDP Growth"]:
    if col in df.columns:
        print(f"\n=== TOP 10 por '{col}' (desc) ===")
        cols_to_show = ["name", col] if "name" in df.columns else [col]
        print(df[cols_to_show].sort_values(col, ascending=False).head(10))

# 5) Correlación rápida (numérico)
num = df.select_dtypes(include="number")
if not num.empty:
    print("\n=== CORRELACIÓN (primeras 8 columnas numéricas) ===")
    print(num.iloc[:, :8].corr().round(3))
else:
    print("\n(No hay columnas numéricas para correlación)")

print("\n✓ Fin del reporte en terminal.")
