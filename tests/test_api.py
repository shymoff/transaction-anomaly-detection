from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_api_returns_http_200():
    response = client.post(
        "/predict",
        json={
            "amount": 5000.0,
            "oldbalanceOrg": 20000.0,
            "newbalanceOrig": 15000.0,
            "oldbalanceDest": 1000.0,
            "newbalanceDest": 6000.0,
            "type_CASH_IN": False,
            "type_CASH_OUT": True,
            "type_DEBIT": False,
            "type_PAYMENT": False,
            "type_TRANSFER": False
        }
    )
    assert response.status_code == 200

def test_predict_fraud_transaction():
    response = client.post(
        "/predict",
        json={
            "amount": 1000000.0,
            "oldbalanceOrg": 1000000.0,
            "newbalanceOrig": 0.0,
            "oldbalanceDest": 0.0,
            "newbalanceDest": 1000000.0,
            "type_CASH_IN": False,
            "type_CASH_OUT": False,
            "type_DEBIT": False,
            "type_PAYMENT": False,
            "type_TRANSFER": True
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "isFraud" in data
    assert isinstance(data["isFraud"], int)
    assert data["isFraud"] in [0, 1]
