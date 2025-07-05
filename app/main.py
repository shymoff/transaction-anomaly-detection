import os
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "model", "randomforest_model.pkl")

model = joblib.load(MODEL_PATH)

class Transaction(BaseModel):
    amount: float
    oldbalanceOrg: float
    newbalanceOrig: float
    oldbalanceDest: float
    newbalanceDest: float
    type_CASH_IN: bool
    type_CASH_OUT: bool
    type_DEBIT: bool
    type_PAYMENT: bool
    type_TRANSFER: bool


@app.post("/predict")
def predict(transaction: Transaction):
    print("Received request with data:", transaction)
    data = np.array([[transaction.amount,
                      transaction.oldbalanceOrg,
                      transaction.newbalanceOrig,
                      transaction.oldbalanceDest,
                      transaction.newbalanceDest,
                      int(transaction.type_CASH_IN),
                      int(transaction.type_CASH_OUT),
                      int(transaction.type_DEBIT),
                      int(transaction.type_PAYMENT),
                      int(transaction.type_TRANSFER)]], dtype=float)
    print(data)
    prediction = model.predict(data)[0]
    return {"isFraud": int(prediction)}
