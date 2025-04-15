import kagglehub
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import ternary
from sklearn.preprocessing import MinMaxScaler
import numpy as np
# Download latest version
path = kagglehub.dataset_download("sumitrodatta/nba-aba-baa-stats")

print("Path to dataset files:", path)


archivo = "Advanced.csv"
archivo2 = "Team Summaries.csv"
file_path = os.path.join(path, archivo)
file_path2= os.path.join(path, archivo2)


df = pd.read_csv(file_path)
df2 = pd.read_csv(file_path2)


latest_season = df['season'].max()
df = df[df['season'] == latest_season]
df2 = df2[df2['season'] == latest_season]


# Calcular Win en Team Summaries
df2['win_percent'] = df2['w'] / (df2['w'] + df2['l'])

# Filtrar jugadores que no tienen equipo definido
df_def = df[df['season'] == latest_season].copy()
df_def = df_def[df_def['tm'] != 'TOT']

# Elegir columnas defensivas
df_def = df[['player', 'tm', 'dws', 'dbpm', 'stl_percent', 'blk_percent', 'drb_percent']].copy()

# Merge con porcentaje de victorias
df_def = df_def.merge(df2[['abbreviation', 'win_percent']], left_on='tm', right_on='abbreviation', how='left')


# Asegúrate de eliminar posibles NaN
df_def_clean = df_def.dropna(subset=['win_percent', 'blk_percent', 'drb_percent', 'stl_percent'])


bins_x = np.linspace(df_def_clean['drb_percent'].min(), df_def_clean['drb_percent'].max(), 20)
bins_y = np.linspace(df_def_clean['blk_percent'].min(), df_def_clean['blk_percent'].max(), 20)


df_def_clean['x_bin'] = pd.cut(df_def_clean['drb_percent'], bins_x, labels=False)
df_def_clean['y_bin'] = pd.cut(df_def_clean['blk_percent'], bins_y, labels=False)


grouped = df_def_clean.groupby(['x_bin', 'y_bin']).agg({
    'drb_percent': 'mean',
    'blk_percent': 'mean',
    'win_percent': 'mean',
    'stl_percent': 'mean'
}).dropna()

# Graficamos
plt.figure(figsize=(10, 8))
scatter = plt.scatter(
    grouped['drb_percent'],
    grouped['blk_percent'],
    c=grouped['win_percent'],
    s=grouped['stl_percent'] * 50, 
    cmap='plasma',
    alpha=0.7,
    edgecolor='k'
)

plt.colorbar(scatter, label='Promedio % de victorias del equipo')
plt.xlabel('Porcentaje de rebotes defensivos (drb_percent)')
plt.ylabel('Porcentaje de bloqueos (blk_percent)')
plt.title('Influencia de estadísticas defensivas en el porcentaje de victorias del equipo\n(Tamaño indica robos - stl_percent)')
plt.grid(True)
plt.tight_layout()
plt.show()