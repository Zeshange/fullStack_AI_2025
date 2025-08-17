import pandas as pd
 import numpy as np
 import tensorflow as tf
 from tensorflow import keras
 from sklearn.preprocessing import MinMaxScaler
 import matplotlib.pyplot as plt

 # 1. Load DJIA dataset
 df = pd.read_csv("C:\Users\Imran Nasir\.cache\kagglehub\datasets\szrlee\stock-time-series-20050101-to-20171231\versions\3")  
 print(df.head())

 # Example: focusing on 'AAPL' Close prices
 data = df['Close'].values.reshape(-1, 1)

 # 2. Normalize data
 scaler = MinMaxScaler(feature_range=(0, 1))
 data_scaled = scaler.fit_transform(data)

 # 3. Create sequences
 def create_sequences(data, seq_length=60):
     X, y = [], []
     for i in range(len(data) - seq_length):
         X.append(data[i:i+seq_length])
         y.append(data[i+seq_length])
     return np.array(X), np.array(y)

 seq_length = 60
 X, y = create_sequences(data_scaled, seq_length)

 # Reshape for LSTM [samples, timesteps, features]
 X = X.reshape(X.shape[0], X.shape[1], 1)

 # 4. Split train-test
 split = int(len(X) * 0.8)
 X_train, X_test = X[:split], X[split:]
 y_train, y_test = y[:split], y[split:]

 # 5. Build LSTM model
 model = keras.Sequential([
     keras.layers.LSTM(50, return_sequences=True, input_shape=(seq_length, 1)),
     keras.layers.LSTM(50),
     keras.layers.Dense(1)  # Predicting price
 ])

 model.compile(optimizer='adam', loss='mean_squared_error')
 # 6. Train
 # model.fit(X_train, y_train, epochs=10, batch_size=32)

# 7. Predict
 predictions = model.predict(X_test)
 predictions = scaler.inverse_transform(predictions)  # Back to original scale
 y_test_actual = scaler.inverse_transform(y_test)

 # 8. Plot results
 plt.figure(figsize=(12,6))
 plt.plot(y_test_actual, color='blue', label='Actual Price')
 plt.plot(predictions, color='red', label='Predicted Price')
 plt.title('Stock Price Prediction')
 plt.xlabel('Time')
 plt.ylabel('Price')
 plt.legend()
 plt.show()


# import kagglehub

# # Download latest version
# path = kagglehub.dataset_download("szrlee/stock-time-series-20050101-to-20171231")

# print("Path to dataset files:", path)