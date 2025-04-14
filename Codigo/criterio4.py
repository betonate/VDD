import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_2024 = pd.read_csv('nba2024.csv')
df_1980 = pd.read_csv('nba1980.csv')

orden_posiciones = ['PG', 'SG', 'SF', 'PF', 'C']

fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharex=True)

sns.boxplot(x='PTS', y='Pos', data=df_2024, order=orden_posiciones, palette="pastel", whis=1.5, fliersize=0, ax=axes[0])
sns.stripplot(x='PTS', y='Pos', data=df_2024, order=orden_posiciones, color='black', size=3, jitter=True, alpha=0.5, ax=axes[0])
axes[0].set_title('NBA 2023-2024')
axes[0].set_xlabel('Puntos por Partido')
axes[0].set_ylabel('Posición')
axes[0].grid(axis='x', linestyle='--', alpha=0.5)

sns.boxplot(x='PTS', y='Pos', data=df_1980, order=orden_posiciones, palette="pastel", whis=1.5, fliersize=0, ax=axes[1])
sns.stripplot(x='PTS', y='Pos', data=df_1980, order=orden_posiciones, color='black', size=3, jitter=True, alpha=0.5, ax=axes[1])
axes[1].set_title('NBA 1979-1980')
axes[1].set_xlabel('Puntos por Partido')
axes[1].set_ylabel('')  # sin etiqueta para ahorrar espacio
axes[1].grid(axis='x', linestyle='--', alpha=0.5)

plt.suptitle('Comparación de Distribución de Puntos por Posición — NBA 1980 vs 2024', fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
