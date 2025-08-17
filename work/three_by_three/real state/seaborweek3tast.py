import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("C:\\Users\\Hp\Documents\\full-stack-ai\\week3\\RealEstate-USA.csv", delimiter =",")

df.info() 
df.dtypes
df.describe() 
df.shape

print(df)

sns.set_theme(style='darkgrid')
sns.lineplot(x='city', y='price', data=df)
plt.show()

sns.catplot(x='city', y='price', data=df)
plt.show()

sns.kdeplot(x='city', y='price', data=df)
plt.show()

sns.scatterplot(x='city', y='price', data=df)
plt.show()

sns.barplot(x='city', y='price', data=df)
plt.show()

df['price'] = pd.to_numeric(df['price'], errors='coerce')
sns.heatmap(x='city', y='price', data=df)
plt.show()

df['price'] = pd.to_numeric(df['price'], errors='coerce')
sns.barplot(x='city', y='price', data=df)
plt.show()

sns.lineplot(x='zip_code', y='price', data=df)
plt.show()

sns.catplot(x='zip_code', y='price', data=df)
plt.show()

sns.kdeplot(x='zip_code', y='price', data=df)
plt.show()

sns.scatterplot(x='zip_code', y='price', data=df)
plt.show()

sns.barplot(x='city', y='price', data=df)
plt.show()

sns.lineplot(x='city', y='price', data=df)
plt.show()

sns.categorical(x='city', y='price', data=df)
plt.show()

df['price'] = pd.to_numeric(df['price'], errors='coerce')
sns.kdeplot(x='city', y='price', data=df)
plt.show()

sns.scatterplot(x='city', y='price', data=df)
plt.show()

sns.barplot(x='city', y='price', data=df)
plt.show()

sns.heatmap(x='city', y='price', data=df)
plt.show()

sns.lineplot(x='acre_lot', y='price', data=df)
plt.show()

sns.catplot(x='acre_lot', y='price', data=df)
plt.show()

sns.scatterplot(x='acre_lot', y='price', data=df)
plt.show()

sns.barplot(x='acre_lot', y='price', data=df)
plt.show()

sns.heatmap(x='acre_lot', y='price', data=df)
plt.show()

