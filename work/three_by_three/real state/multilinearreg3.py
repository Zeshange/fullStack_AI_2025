import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\Hp\\Downloads\\mtcars.csv")

df.info()
df.dtypes
df.describe()
df.shape

print(df.columns)


x = df[['mpg','cyl','disp']].values
y = df['hp'].values


sns.regplot(x='mpg', y='hp', data=df,)
plt.title('Miles per Gallon vs Horsepower')
plt.show()

sns.regplot(x='cyl', y='hp', data=df)
plt.title('Cylinders vs Horsepower')
plt.show()

sns.regplot(x='disp', y='hp', data=df)
plt.title('Displacement vs Horsepower')
plt.show()


corr_matrix = df[['mpg','cyl','disp','hp']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
SEED = 42
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)

print("intercept:", model.intercept_)
print("slope:", model.coef_)

y_pred = model.predict(x_test)
from sklearn.metrics import mean_squared_error, mean_absolute_error
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)


print("Mean Squared Error:", mse)
print("Mean Absolute Error:", mae)

