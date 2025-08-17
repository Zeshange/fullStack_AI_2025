#  Import Required Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#  Load Dataset
df = pd.read_csv("startup_growth_investment_data.csv")


# Drop rows with missing values in critical numeric columns
df.dropna(subset=['Valuation (USD)', 'Investment Amount (USD)'], inplace=True)

# Ensure numeric fields are of correct type
df['Year Founded'] = pd.to_numeric(df['Year Founded'], errors='coerce')
df['Valuation (USD)'] = pd.to_numeric(df['Valuation (USD)'], errors='coerce')
df['Investment Amount (USD)'] = pd.to_numeric(df['Investment Amount (USD)'], errors='coerce')

# Update again after coercing types (to drop NaNs introduced)
df.dropna(subset=['Valuation (USD)', 'Investment Amount (USD)'], inplace=True)

#  Set Plot Style
sns.set(style="whitegrid")
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12


#  Count Plot: Number of Startups by Country

plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Country', order=df['Country'].value_counts().index)
plt.title(" Number of Startups by Country")
plt.xlabel("Country")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#  Bar Plot: Average Valuation (USD) by Country

plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='Country', y='Valuation (USD)', estimator='mean', ci=None)
plt.title(" Average Valuation by Country")
plt.xlabel("Country")
plt.ylabel("Average Valuation (USD)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#  Box Plot: Investment Amount by Country

plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Country', y='Investment Amount (USD)')
plt.title(" Investment Distribution by Country")
plt.xlabel("Country")
plt.ylabel("Investment Amount (USD)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#  Histogram: Distribution of Startup Valuations

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Valuation (USD)', kde=True, bins=30)
plt.title(" Distribution of Startup Valuations")
plt.xlabel("Valuation (USD)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


#  Scatter Plot: Investment vs. Valuation (Colored by Country)

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Investment Amount (USD)', y='Valuation (USD)', hue='Country')
plt.title(" Investment vs Valuation (USD)")
plt.xlabel("Investment Amount (USD)")
plt.ylabel("Valuation (USD)")
plt.tight_layout()
plt.show()


#  Heatmap: Correlation Between Numeric Columns

plt.figure(figsize=(8, 6))
corr = df.select_dtypes(include='number').corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title(" Correlation Heatmap")
plt.tight_layout()
plt.show()
