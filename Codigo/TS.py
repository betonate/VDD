import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Team_Summaries.csv")

df_2025 = df[df["season"] == 2025].copy()

df_2025["w"] = pd.to_numeric(df_2025["w"], errors="coerce")
df_2025["pw"] = pd.to_numeric(df_2025["pw"], errors="coerce")

df_2025 = df_2025.dropna(subset=["w", "pw"])
df_2025["diff"] = df_2025["w"] - df_2025["pw"]

df_2025 = df_2025.sort_values("diff")

fig, ax = plt.subplots(figsize=(8, 10))

for idx, row in df_2025.iterrows():
    ax.plot([row["pw"], row["w"]], [row["team"], row["team"]], color="lightgray", linewidth=1.5)

ax.scatter(df_2025["pw"], df_2025["team"], color="steelblue", label="Victorias esperadas", s=50)
ax.scatter(df_2025["w"], df_2025["team"], color="seagreen", label="Victorias reales", s=50)

# Etiquetas y estética
ax.set_title("Comparación de Victorias Reales vs. Esperadas - NBA 2025", fontsize=13, weight="bold")
ax.set_xlabel("Cantidad de Victorias")
ax.tick_params(axis='y', labelsize=7)
ax.legend(fontsize=9)

plt.tight_layout()
plt.savefig("dumbbell_plot_nba2025_victorias.png", dpi=300)  # 💾 Guardar imagen opcional
plt.show()
