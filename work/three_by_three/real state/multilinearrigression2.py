import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\Hp\\Downloads\\Real_Estate_Sales_2001-2022_GL-Short (1).csv")

df.info()
df.dtypes
df.describe()
df.shape

print(df.columns)


x = df[['Serial Number','List Year','Assessed Value']].values
y = df['Sale Amount'].values


sns.regplot(x='Serial Number', y='Sale Amount', data=df,)
plt.title('Serial Number vs Sale Amount')
plt.show()

sns.regplot(x='List Year', y='Sale Amount', data=df)
plt.title('List Year vs Sale Amount')
plt.show()

sns.regplot(x='Assessed Value', y='Sale Amount', data=df)
plt.title('Date Recorded vs Sale Amount')
plt.show()


corr_matrix = df[['Serial Number','List Year','Assessed Value', 'Sale Amount']].corr()
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

