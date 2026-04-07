
---
# Transaction Risk ML – Real-Time Risk Scoring System

## Overview

This project implements a **real-time transaction risk scoring system** using machine learning.

It predicts the **fraud risk probability** of a transaction and maps it into actionable decisions:

- **ALLOW** → Low risk  
- **CHALLENGE** → Medium risk  
- **BLOCK** → High risk  

The system demonstrates a **production-style ML workflow** with separate training and inference pipelines.

---

## Key Features

- End-to-end ML pipeline (training → inference)
- Logistic Regression baseline model
- Real-time inference using FastAPI
- Dockerized for deployment
- Clean separation between training and serving
- Scenario-based validation for risk decisions

---

## Model Summary

- Model: Logistic Regression  
- Preprocessing: StandardScaler  
- Training Data: Synthetic dataset with realistic fraud patterns  
- ROC-AUC: ~0.93  

The model outputs a **risk probability**, which is converted into business decisions using thresholding.

---

## Project Structure

```
transaction-risk-ml/
│
├── data/
├── training/            # Training pipeline
├── inference/           # API & inference logic
├── models/              # Model artifacts
├── system_design.md     # Architecture documentation
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## Running the Project

### Install dependencies

```bash
pip install -r requirements.txt
```

### Train model

```bash
python training/train.py
```

### Run inference API

```bash
uvicorn inference.app:app --reload
```

API:

```
http://127.0.0.1:8000/docs
```
---
## 🌐 Live API

The model is deployed and accessible via a public API.

**Base URL:**
https://transaction-risk-ml-production-system.onrender.com

**Interactive Docs (Swagger UI):**
https://transaction-risk-ml-production-system.onrender.com/docs

You can test the API directly from the Swagger interface without any setup.

---

## Example Request

json
{
  "amount": 2500,
  "account_age_days": 180,
  "past_txn_count_24h": 5,
  "hour_of_day": 22,
  "merchant_risk_score": 0.5
}

---
Example Response

{
  "risk_score": 0.47,
  "decision": "CHALLENGE"
}

---

## Deployment

```bash
docker build -t <username>/transaction-risk-ml .
docker run -p 10000:10000 <username>/transaction-risk-ml
```

---

## Dataset

The dataset used for training is synthetic and not included in this repository.

It was designed to simulate realistic fraud scenarios using:

Transaction behavior

Account characteristics

Merchant risk signals

---
## Model Performance

The model is evaluated using ROC-AUC on a validation split.

- **Model**: Logistic Regression
- **ROC-AUC Score**: ~0.93
- **Pipeline**: StandardScaler + Logistic Regression

Note: The dataset is synthetically generated with controlled noise to simulate real-world variability and avoid feature dominance.
---

## Documentation

Detailed system architecture, design decisions, and trade-offs are available in:

**Detailed System Design**  
  → [Open](system_design.md)

---
