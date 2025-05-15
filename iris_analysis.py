# iris_analysis.py

import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore
from sklearn.datasets import load_iris # type: ignore

# Load and explore the dataset
try:
    iris = load_iris(as_frame=True)
    df = iris.frame
    print("Dataset loaded successfully.")
except Exception as e:
    print(f"Error loading dataset: {e}")
    exit()

# Display first few rows
print("\nFirst 5 rows:")
print(df.head())

# Data types and missing values
print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

# Statistical summary
print("\nDescriptive Statistics:")
print(df.describe())

# Group by species (target) and calculate mean
df['species'] = df['target'].map(dict(enumerate(iris.target_names)))
grouped = df.groupby('species').mean()
print("\nMean values by species:")
print(grouped)

# ----- Visualization Section -----

sns.set(style="whitegrid")  # nice seaborn style

# 1. Line Chart - mean of features per species
grouped.T.plot(marker='o')
plt.title("Mean Feature Values per Species")
plt.xlabel("Features")
plt.ylabel("Mean (cm)")
plt.legend(title='Species')
plt.tight_layout()
plt.show()

# 2. Bar Chart - average petal length per species
sns.barplot(x='species', y='petal length (cm)', data=df)
plt.title("Average Petal Length by Species")
plt.tight_layout()
plt.show()

# 3. Histogram - sepal length distribution
sns.histplot(df['sepal length (cm)'], kde=True, bins=10)
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.tight_layout()
plt.show()

# 4. Scatter Plot - Sepal vs Petal Length
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.title("Sepal Length vs Petal Length")
plt.tight_layout()
plt.show()
