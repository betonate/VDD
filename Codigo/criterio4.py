import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('nba.csv')

plt.figure(figsize=(10,6))


sns.boxplot(x='PTS', y='Pos', data=df, palette="pastel", whis=1.5, fliersize=0)


sns.stripplot(x='PTS', y='Pos', data=df, color='black', size=4, jitter=True, alpha=0.6)

plt.title('Distribución de Puntos por Partido según Posición - NBA', fontsize=14)
plt.xlabel('Puntos por Partido')
plt.ylabel('Posición')
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
