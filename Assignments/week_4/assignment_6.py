import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Read dataset
df = pd.read_csv("Assignments\\week_4\\mtcars.csv")

# Display basic info
print(df.head())
print(df.info())
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())

# Bar plot of mpg by model
plt.figure(figsize=(10,5))
sns.barplot(x='model', y='mpg', data=df)
plt.xticks(rotation=90)
plt.title('Miles Per Gallon (MPG) by Car Model', fontsize=14, fontweight='bold')
plt.xlabel('Car Model')
plt.ylabel('MPG')
plt.tight_layout()
plt.show()

# Features and target
X = df.drop(columns=['mpg', 'model'])
y = df['mpg']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=42, test_size=0.2
)

# Model training
reg = LinearRegression()
reg.fit(X_train, y_train)
y_predict = reg.predict(X_test)

# Create DataFrame for results
predicted_df = pd.DataFrame({
    "actual": y_test.squeeze(),
    "predicted": y_predict.squeeze()
})

# Calculate metrics
r2 = r2_score(y_test, y_predict)
mae = mean_absolute_error(y_test, y_predict)
rmse = np.sqrt(mean_squared_error(y_test, y_predict))

#  scatter plot
# sns.set_style("whitegrid")
plt.figure(figsize=(7, 6))
sns.scatterplot(x="actual", y="predicted", data=predicted_df)

# Add diagonal reference line
max_val = max(predicted_df.max())
min_val = min(predicted_df.min())
plt.plot([min_val, max_val], [min_val, max_val])

# Labels & title
plt.title("Actual vs Predicted MPG", fontsize=16, fontweight='bold')
plt.xlabel("Actual MPG", fontsize=12)
plt.ylabel("Predicted MPG", fontsize=12)
plt.legend()



plt.tight_layout()
plt.show()

