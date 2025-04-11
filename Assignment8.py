import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('C:/Users/desir/Downloads/Exercise_Data.csv')

# --- HEATMAP: Average 30-min pulse by diet and kind (exercise type) ---
heatmap_data = df.pivot_table(values='30 min', index='diet', columns='kind', aggfunc='mean')

plt.figure(figsize=(8, 5))
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', fmt=".1f")
plt.title("Average 30-Minute Pulse by Diet and Exercise Type")
plt.xlabel("Exercise Type")
plt.ylabel("Diet Type")
plt.tight_layout()
plt.show()

# --- CATEGORICAL PLOT: 30-min pulse by diet ---
plt.figure(figsize=(8, 5))
sns.boxplot(x='diet', y='30 min', data=df)
plt.title("30-Minute Pulse by Diet Type")
plt.xlabel("Diet")
plt.ylabel("Pulse (30 min)")
plt.tight_layout()
plt.show()

# --- CATEGORICAL PLOT: 30-min pulse by kind ---
plt.figure(figsize=(8, 5))
sns.boxplot(x='kind', y='30 min', data=df)
plt.title("30-Minute Pulse by Exercise Type")
plt.xlabel("Exercise Type")
plt.ylabel("Pulse (30 min)")
plt.tight_layout()
plt.show()


planets = sns.load_dataset("planets")

plt.figure(figsize=(8, 5))
sns.scatterplot(data=planets, x="distance", y="orbital_period", hue="method")
plt.title("Orbital Period vs Distance by Detection Method")
plt.xlabel("Distance (light years)")
plt.ylabel("Orbital Period (days)")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.lineplot(data=planets.groupby("year").size().reset_index(name="discoveries"), x="year", y="discoveries")
plt.title("Exoplanet Discoveries Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Discoveries")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(data=planets, x="mass", bins=30, kde=True)
plt.title("Distribution of Exoplanet Mass")
plt.xlabel("Mass (Jupiter Masses)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=planets, x="method", y="mass")
plt.title("Planet Mass by Detection Method")
plt.xlabel("Detection Method")
plt.ylabel("Mass (Jupiter Masses)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=planets, y="method", order=planets["method"].value_counts().index)
plt.title("Number of Discoveries by Method")
plt.xlabel("Count")
plt.ylabel("Detection Method")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=planets, x="method", y="orbital_period", estimator='mean')
plt.title("Mean Orbital Period by Detection Method")
plt.xlabel("Detection Method")
plt.ylabel("Average Orbital Period (days)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


