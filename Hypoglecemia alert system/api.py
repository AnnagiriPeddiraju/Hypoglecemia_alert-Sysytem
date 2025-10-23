from fastapi import FastAPI, Request
import tensorflow as tf
import numpy as np

app = FastAPI()
model = tf.keras.models.load_model("model.h5")

@app.post("/predict")
async def predict(request: Request):
    payload = await request.json()
    data = np.array(payload["data"]).reshape((-1, 12, 1))  # 12 time-steps as required by model
    pred = model.predict(data)
    return {"risk": float(pred[0][0])}