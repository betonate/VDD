import pandas as pd
import matplotlib.pyplot as plt

# Cargar archivo
df = pd.read_csv("Team_Summaries.csv")

# Filtrar temporada 2025 y columnas necesarias
df = df[df["season"] == 2025][["team", "tov_percent", "l"]]

# Asegurar que los datos sean numéricos
df["tov_percent"] = pd.to_numeric(df["tov_percent"], errors="coerce")
df["l"] = pd.to_numeric(df["l"], errors="coerce")
df = df.dropna()

# Ordenar por tov_percent
df = df.sort_values("tov_percent")

# Crear gráfico tipo lollipop con nombres de los equipos sin solapamiento
plt.figure(figsize=(12, 8))

for i, row in enumerate(df.itertuples()):
    plt.plot([row.tov_percent, row.tov_percent], [0, row.l], color='gray', linewidth=1)
    plt.plot(row.tov_percent, row.l, 'o', color='firebrick')
    offset = 0.8 if i % 2 == 0 else -1.0  # alternar etiquetas arriba y abajo
    plt.text(row.tov_percent + 0.05, row.l + offset, row.team, fontsize=6)

plt.title("Relaci\u00f3n entre Tasa de P\u00e9rdidas por Posesi\u00f3n (TOV%) y Derrotas - NBA 2025", fontsize=14, weight="bold")
plt.xlabel("Tasa de P\u00e9rdidas por Posesi\u00f3n (%)")
plt.ylabel("Cantidad de Derrotas")
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("lollipop_plot_tov_vs_derrotas.png", dpi=300)
plt.show()