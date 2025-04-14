import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Leer el archivo CSV
df = pd.read_csv("Team_Stats_Per_Game.csv")

# 2. Asegurar que 'pts_per_game' sea numérico y eliminar filas vacías
df["pts_per_game"] = pd.to_numeric(df["pts_per_game"], errors="coerce")
df_clean = df.dropna(subset=["pts_per_game"])

# 3. Crear el gráfico de violín
plt.figure(figsize=(10, 6))
sns.violinplot(data=df_clean, x="pts_per_game", inner="quartile", color="skyblue")

# 4. Personalización del gráfico
plt.title("Distribución del promedio de puntos por equipo - NBA 2025", fontsize=14, weight='bold')
plt.xlabel("Puntos por partido")
plt.yticks([])  # Ocultar eje Y porque no es relevante en este caso

# 5. Guardar el gráfico como imagen PNG
plt.tight_layout()
plt.savefig("violinplot_pts_per_game_nba2025.png", dpi=300)  # 📁 Guardado en alta calidad

# 6. Mostrar el gráfico en pantalla
plt.show()
