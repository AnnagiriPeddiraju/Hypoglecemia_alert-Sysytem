# Hypoglycemia Predictor Frontend

A simple React web interface for submitting glucose data and viewing hypoglycemia risk.

## Setup

```sh
cd frontend
npm install
npm start
```

## Usage

- Enter the last 12 glucose readings.
- Click "Predict Risk" to see the predicted risk of hypoglycemia.

## API

This app expects a backend endpoint at `/predict` (see main repo for API server).