# Hypoglycemia Prediction & Smart Alert Notification System

This project predicts hypoglycemic events using deep learning and provides a web interface for risk prediction.

## Features

- Time-series prediction using LSTM (TensorFlow/Keras)
- Simulated CGM data pipeline (replace with real sources)
- REST API for model inference (FastAPI)
- React frontend for user input and results
- Dockerized backend for easy deployment

## Setup

### 1. Clone the repo & install backend dependencies
```sh
git clone https://github.com/yourusername/hypoglycemia-predictor.git
cd hypoglycemia-predictor
pip install -r requirements.txt
```

### 2. Train & save the model
```sh
python hypoglycemia_predictor.py
```
This will simulate data, train the model, and save `model.h5`.

### 3. Run the API server
```sh
uvicorn api:app --host 0.0.0.0 --port 8000
```

### 4. Setup & run the frontend
```sh
cd frontend
npm install
npm start
```
For local development, add `"proxy": "http://localhost:8000"` to `frontend/package.json` so requests to `/predict` go to your backend.

### 5. Docker deployment (backend only)
```sh
docker build -t hypoglycemia-predictor .
docker run -d -p 80:80 hypoglycemia-predictor
```

## Usage

- Enter your latest 12 glucose readings in the frontend.
- Click "Predict Risk" to see your hypoglycemia risk.

---

## License
MIT