
---

# Transaction Risk ML – Real-Time Risk Scoring System

## Overview

This project implements a **real-time transaction risk scoring ML system** demonstrating production-style ML architecture: offline training, model versioning, and containerized online inference.

The system predicts the **fraud/risk probability of financial transactions** and exposes a **FastAPI inference endpoint** for real-time scoring.

---

## Key Features

* End-to-end ML pipeline (data → training → inference)
* Logistic Regression baseline scoring model
* Experiment tracking using **MLflow**
* Real-time inference via **FastAPI**
* **Dockerized** deployment
* System design documentation (`system_design.md`)

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

## Deployment

```bash
docker build -t <username>/transaction-risk-ml .
docker run -p 8000:8000 <username>/transaction-risk-ml
```

---

## Documentation

Detailed system architecture, design decisions, and trade-offs are available in:

**system_design.md**

---
