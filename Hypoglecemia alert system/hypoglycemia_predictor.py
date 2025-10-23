import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Dummy CGM data simulation
def load_data():
    # Replace with actual data loading
    timestamps = pd.date_range("2023-01-01", periods=1000, freq="5T")
    glucose = np.random.normal(loc=100, scale=30, size=len(timestamps))
    # Simulate hypoglycemia events
    glucose[::200] = np.random.uniform(40, 60, size=5)
    data = pd.DataFrame({"timestamp": timestamps, "glucose": glucose})
    return data

def preprocess(data, timesteps=12):
    # Normalize glucose
    data["glucose_norm"] = (data["glucose"] - data["glucose"].mean()) / data["glucose"].std()
    X, y = [], []
    for i in range(len(data) - timesteps):
        X.append(data["glucose_norm"].iloc[i:i+timesteps].values)
        # Label: next value is hypoglycemia (<70 mg/dL)
        y.append(int(data["glucose"].iloc[i+timesteps] < 70))
    X = np.array(X)
    y = np.array(y)
    return X, y

def build_model(timesteps):
    model = Sequential([
        LSTM(64, input_shape=(timesteps, 1), return_sequences=True),
        LSTM(32),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def train_and_predict():
    data = load_data()
    timesteps = 12
    X, y = preprocess(data, timesteps)
    X = X.reshape((-1, timesteps, 1))
    split = int(0.8 * len(X))
    X_train, y_train = X[:split], y[:split]
    X_test, y_test = X[split:], y[split:]
    model = build_model(timesteps)
    model.fit(X_train, y_train, epochs=10, batch_size=32)
    preds = model.predict(X_test)
    model.save("model.h5")  # Save model for API use
    return preds, y_test, data.iloc[split+timesteps:]

def send_alert(pred, threshold=0.5, timestamp=None):
    if pred > threshold:
        print(f"ALERT: High risk of hypoglycemia predicted at {timestamp}")
    else:
        print(f"No hypoglycemia risk at {timestamp}")

# Run prototype
if __name__ == "__main__":
    preds, y_test, timestamps = train_and_predict()
    for p, t in zip(preds, timestamps["timestamp"]):
        send_alert(p, timestamp=t)