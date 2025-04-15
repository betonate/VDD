import kagglehub
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


path = kagglehub.dataset_download("sumitrodatta/nba-aba-baa-stats")
print("Path to dataset files:", path)

# Archivos relevantes
archivo_jugadores = "Advanced.csv"
archivo_equipos = "Team Summaries.csv"
file_path_jugadores = os.path.join(path, archivo_jugadores)
file_path_equipos = os.path.join(path, archivo_equipos)

df = pd.read_csv(file_path_jugadores)
df2 = pd.read_csv(file_path_equipos)

latest_season = df['season'].max()
df = df[df['season'] == latest_season]
df2 = df2[df2['season'] == latest_season]

df2['win_percent'] = df2['w'] / (df2['w'] + df2['l'])

df_def = df[['player', 'tm', 'dws']].copy()
df_def = df_def[df_def['tm'] != 'TOT']

df_def = df_def.merge(df2[['abbreviation', 'win_percent']], left_on='tm', right_on='abbreviation', how='left')

df_def_clean = df_def.dropna(subset=['dws', 'win_percent'])

df_def_clean['dws_rounded'] = df_def_clean['dws'].round(1)

plt.figure(figsize=(12, 6))
sns.swarmplot(data=df_def_clean, x='dws_rounded', y='win_percent', size=5, color='dodgerblue')

# Etiquetas y título
plt.title('Distribución de Porcentaje de Victorias según DWS (swarmplot)', fontsize=14)
plt.xlabel('Defensive Win Shares (DWS) - Redondeado')
plt.ylabel('Win Percentage')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
