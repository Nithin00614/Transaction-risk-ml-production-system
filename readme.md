
# Transaction Risk ML – Real-Time Risk Scoring System

## Overview

This project implements a **real-time transaction risk scoring ML system** designed to demonstrate practical **ML system design principles**, including offline training, online inference, model versioning, monitoring, and deployment readiness.

The system predicts the **fraud / risk probability of financial transactions** using structured transaction features and exposes a **FastAPI inference endpoint** for real-time scoring.

---

## Key Features

* End-to-end ML pipeline (data → training → inference)
* Logistic Regression baseline risk scoring model
* Offline training and experiment tracking with **MLflow**
* Real-time inference using **FastAPI**
* Containerized deployment using **Docker**
* Monitoring-ready logging architecture
* Clear **system design documentation** (`system_design.md`)

---

## Project Structure

```
transaction-risk-ml/
│
├── data/                  # Sample dataset
├── src/
│   ├── train.py           # Training pipeline
│   ├── inference.py       # Inference logic
│   ├── app.py             # FastAPI service
│
├── models/                # Saved model artifacts
├── system_design.md       # System architecture & decisions
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## ML System Architecture

The system follows a **production-style ML architecture**:

* **Offline layer:** model training, validation, experiment tracking
* **Online layer:** stateless inference API for real-time predictions
* **Monitoring layer:** logging hooks for operational and prediction monitoring
* **Deployment layer:** Dockerized container ready for EC2 / cloud deployment

Detailed architecture and trade-off decisions are documented in
`system_design.md`.

---

## Running the Project

### Install dependencies

```bash
pip install -r requirements.txt
```

### Train model

```bash
python src/train.py
```

### Run inference API

```bash
uvicorn src.app:app --reload
```

API will be available at:

```
http://127.0.0.1:8000/docs
```

---

## Deployment

The application is containerized using Docker and can be deployed locally or on cloud infrastructure (e.g., AWS EC2).

```bash
docker build -t <username>/transaction-risk-ml .
docker run -p 8000:8000 <username>/transaction-risk-ml
```

---

## Purpose of the Project

This project is designed to:

* Demonstrate **practical ML system design thinking**
* Showcase **real-time ML inference architecture**
* Provide a **portfolio-ready example** of deployable ML systems

---

## Documentation

For full architecture details, design decisions, trade-offs, and failure-handling strategies, see:

**`system_design.md`**

---


