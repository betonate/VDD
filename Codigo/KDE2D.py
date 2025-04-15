import kagglehub
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

path = kagglehub.dataset_download("sumitrodatta/nba-aba-baa-stats")
print("Path to dataset files:", path)

archivo_jugadores = "Advanced.csv"
archivo_equipos = "Team Summaries.csv"
file_path_jugadores = os.path.join(path, archivo_jugadores)
file_path_equipos = os.path.join(path, archivo_equipos)

df = pd.read_csv(file_path_jugadores)
df2 = pd.read_csv(file_path_equipos)

latest_season = df['season'].max()
df = df[df['season'] == latest_season]
df2 = df2[df2['season'] == latest_season]

df2['loss_percent'] = df2['l'] / (df2['w'] + df2['l'])

df_def = df[['player', 'tm', 'stl_percent']].copy()
df_def = df_def[df_def['tm'] != 'TOT']  # Eliminar jugadores con múltiples equipos

df_def = df_def.merge(df2[['abbreviation', 'loss_percent']], left_on='tm', right_on='abbreviation', how='left')

df_def = df_def.dropna(subset=['stl_percent', 'loss_percent'])

plt.figure(figsize=(10, 6))
sns.kdeplot(
    data=df_def,
    x="stl_percent", 
    y="loss_percent",
    fill=True,
    cmap="magma", 
    thresh=0.01,
    levels=100
)

# Etiquetas
plt.xlabel('Porcentaje de Robos (STL%)')
plt.ylabel('Porcentaje de Derrotas del Equipo')
plt.title('Densidad de STL% vs Derrotas del Equipo (KDE Plot)')

# Mostrar
plt.tight_layout()
plt.show()