# Transaction Fraud Detection

Projekt wykrywania oszustw finansowych w transakcjach (fraud detection) przy użyciu modeli ml. Model został wytrenowany na danych z symulacji PaySim i udostępniony poprzez REST API zbudowane w FastAPI.

---

## 📂 Struktura projektu

```
transaction-anomaly-detection/
├── app/
│   └── main.py
├── model/
│   └── randomforest_model.pkl
├── notebooks/
│   ├── eda.ipynb
│   └── model_training.ipynb
├── tests/
│   └── test_api.py
├── requirements.txt
└── README.md
```

---

## 🔍 Dane

Dane pochodzą z symulatora transakcji [PaySim](https://www.kaggle.com/datasets/ealaxi/paysim1). W notebooku eda.ipynb wykonano analizę danych i przygotowano dane do trenowania modelu (m.in. one-hot encoding dla typu transakcji, usunięcie ID).

---

## 🧠 Model

### ✅ Użyte modele:

- RandomForestClassifier (skonfigurowany przez GridSearch, najlepszy wynik)

- LightGBM

- LogisticRegression

Ostateczny model to RandomForest z F1-score ≈ 0.74 na testowym zbiorze danych.

Model zapisano w model/randomforest_model.pkl (serializacja przez joblib).

---

## 🚀 API

Aplikacja FastAPI udostępnia endpoint do predykcji:
POST /predict

### 🔧 Przykładowe zapytanie
```
{
  "amount": 5000.0,
  "oldbalanceOrg": 20000.0,
  "newbalanceOrig": 15000.0,
  "oldbalanceDest": 1000.0,
  "newbalanceDest": 6000.0,
  "type_CASH_IN": false,
  "type_CASH_OUT": true,
  "type_DEBIT": false,
  "type_PAYMENT": false,
  "type_TRANSFER": false
}
```

### ✅ Przykładowa odpowiedź

```
{
  "isFraud": 0
}
```

Gdzie isFraud to:
- 1 – transakcja podejrzana (oszustwo)
- 0 – transakcja prawidłowa