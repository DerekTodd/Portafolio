# -------------------------------------------------------------
# 📊 Visualización automática del dataset NBA (versión corregida)
# Autor: Derek Todd
# -------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import os

# 1️⃣ Cargar el dataset
archivo = "nba.csv"
if not os.path.exists(archivo):
    raise FileNotFoundError("El archivo nba.csv no se encontró en el directorio actual.")

df = pd.read_csv(archivo)

# 2️⃣ Limpiar datos (evita errores con valores vacíos o numéricos)
df = df.dropna(how='all')  # eliminar filas completamente vacías
df = df.fillna('Desconocido')  # reemplazar vacíos por texto

# Convertir columnas categóricas a string (por seguridad)
for col in df.select_dtypes(include=['object', 'float64', 'int64']).columns:
    df[col] = df[col].astype(str)

# 3️⃣ Detectar tipos de columnas
columnas_categoricas = df.select_dtypes(include=["object"]).columns.tolist()
columnas_numericas = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

print("✅ Dataset cargado correctamente\n")
print("Columnas categóricas:", columnas_categoricas)
print("Columnas numéricas:", columnas_numericas, "\n")

# 4️⃣ Gráfica de barras
col_cat = None
for c in ["Team", "Pos", "Position"]:
    if c in columnas_categoricas:
        col_cat = c
        break

col_num = None
for c in ["Points", "PTS", "Salary", "Height", "Weight"]:
    if c in df.columns:
        try:
            df[c] = pd.to_numeric(df[c], errors='coerce')
            col_num = c
            break
        except:
            continue

if col_cat and col_num:
    plt.figure(figsize=(10,5))
    df.groupby(col_cat)[col_num].mean().sort_values(ascending=False).plot(kind='bar', color='skyblue')
    plt.title(f"Promedio de {col_num} por {col_cat}")
    plt.ylabel(f"Promedio de {col_num}")
    plt.xlabel(col_cat)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("barras.png")
    plt.show()
    print("📊 Gráfica de barras generada: barras.png\n")

# 5️⃣ Gráfica de dispersión
if "Weight" in df.columns and "Height" in df.columns:
    df["Weight"] = pd.to_numeric(df["Weight"], errors='coerce')
    df["Height"] = pd.to_numeric(df["Height"], errors='coerce')
    plt.figure(figsize=(7,5))
    plt.scatter(df["Weight"], df["Height"], alpha=0.6)
    plt.title("Relación entre Peso y Altura de jugadores")
    plt.xlabel("Peso")
    plt.ylabel("Altura")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig("dispersion.png")
    plt.show()
    print("⚽ Gráfica de dispersión generada: dispersion.png\n")

# 6️⃣ Gráfica de pastel
if "Team" in df.columns:
    conteo = df["Team"].value_counts().head(10)
    plt.figure(figsize=(8,8))
    conteo.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title("Distribución de jugadores por equipo (Top 10)")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("pastel.png")
    plt.show()
    print("🥧 Gráfica de pastel generada: pastel.png\n")

print("✅ Proceso completado correctamente.")
