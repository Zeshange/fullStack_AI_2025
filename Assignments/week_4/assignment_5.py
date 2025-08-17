import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Assignments//week_4//housing.csv")

# Fill missing values in 'total_bedrooms' with median
df['total_bedrooms'] = df['total_bedrooms'].fillna(df['total_bedrooms'].median())

# One-hot encode categorical column
df = pd.get_dummies(df, columns=['ocean_proximity'], drop_first=True)

# Prepare features and target
X = df.drop(columns=['median_income', 'median_house_value'])
y = df['median_house_value']

# Plot lineplot
# sns.scatterplot(x='total_rooms', y='median_house_value', data=df, alpha=0.5)
# plt.xlabel('Total Rooms')
# plt.ylabel('Median House Value')
# plt.title('Housing Data: Total Rooms vs Median House Value')
# plt.show()
# Print target values
# print(y)

from sklearn.model_selection import train_test_split

X_train,X_text,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(X_train,y_train)
y_Predict=reg.predict(X_text)

df_predicted=pd.DataFrame({'Actual':y_test.squeeze(),'Pridicted':y_Predict.squeeze()})

print(df_predicted)

sns.scatterplot(x='Actual',y='Pridicted',data=df_predicted)
sns.lineplot(x='Actual',y='Pridicted',data=df_predicted)
plt.show()
print(df_predicted)

print(reg.coef_)
print(reg.intercept_)


from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score

import numpy as np

mae = mean_absolute_error(y_test, y_Predict)
mse = mean_squared_error(y_test, y_Predict)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_Predict)


print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')
print(f'R2 Score: {r2:.2f}')

