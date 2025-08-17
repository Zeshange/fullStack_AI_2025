import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.metrics import MeanSquaredError, MeanAbsoluteError
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("work\\fridayTask\\all_stocks_2006-01-01_to_2018-01-01.csv")
df = df.drop("Name", axis=1)
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date').sort_index()

# Scaler for all features
scaler = MinMaxScaler()
df[['Open','High','Low','Close','Volume']] = scaler.fit_transform(df[['Open','High','Low','Close','Volume']])

# Separate scaler for Close (target)
scaler_close = MinMaxScaler()
df[['Close']] = scaler_close.fit_transform(df[['Close']])

# Features and target
X = df.drop('Close', axis=1).values
y = df['Close'].values

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Reshape for LSTM (samples, timesteps, features)
X_train = np.expand_dims(X_train, axis=1)  # timestep = 1
X_test = np.expand_dims(X_test, axis=1)

# Build model
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(LSTM(units=50))
model.add(Dense(1))

# Compile with regression metrics
model.compile(optimizer='adam', loss='mse', metrics=[MeanSquaredError(), MeanAbsoluteError()])

# Train
history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1)

# Predict
predictions = model.predict(X_test)

# Inverse scale predictions and actual values
predictions = scaler_close.inverse_transform(predictions)
y_test = scaler_close.inverse_transform(y_test.reshape(-1,1))

# RMSE
rmse = np.sqrt(np.mean((y_test.flatten() - predictions.flatten())**2))
print(f'RMSE: {rmse:.2f}')
