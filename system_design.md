# Transaction Risk Scoring ML System

## 1. Problem Overview
This system provides real-time fraud risk scoring for incoming
payment transactions. The output is a probability score used by
downstream services to allow, challenge, or block transactions.

The system is designed to be lightweight, stateless, and low-latency.

---

## 2. Functional Requirements
- Accept transaction features via HTTP API
- Return fraud risk score in real time
- Support threshold-based decisions

---

## 3. Non-Functional Requirements
- P99 latency < 50 ms
- Stateless inference service
- Horizontally scalable
- High availability

---

## 4. Data & Feature Design

### Offline Features
- Merchant risk score
- Historical fraud patterns
- Feature distributions

Computed during offline training and baked into the model.

### Online Features
- Transaction amount
- Hour of day
- Account age
- Recent transaction count

All online features are lightweight and deterministic.

---

## 5. ML Approach
- Binary classification (fraud / not fraud)
- Logistic Regression as baseline
- Probability output used for decisions
- Thresholds controlled outside ML

---

## 6. System Architecture

Offline Pipeline:
- Data ingestion
- Feature engineering
- Model training
- Model evaluation
- Model versioning via MLflow

Online Pipeline:
- FastAPI service
- Input validation
- Feature vector construction
- In-memory model inference
- JSON response

---

## 7. Offline vs Online Separation
Training and inference code paths are strictly separated to avoid
training-serving skew and accidental coupling.

---

## 8. API Design
POST /score

Request:
- Stateless JSON payload
- No user session dependency

Response:
- Risk score
- Decision label
- Model version

---

## 9. Scalability (Conceptual)
- Stateless service enables horizontal scaling
- Load balancer distributes traffic
- Each instance loads model once at startup
- No shared state between instances

---

## 10. Latency Considerations
- Simple model choice
- No database calls in inference path
- Minimal feature transformations
- Model loaded in memory

---

## 11. Failure Handling
- Invalid input rejected at schema validation
- Model load failure prevents service startup
- Timeouts handled at API gateway layer

---

## 12. Trade-offs
- Simpler model chosen over deep learning for reliability
- No real-time feature store to reduce latency
- Accuracy traded for predictability

---

## 13. Limitations
- No concept drift detection
- No online learning
- No streaming ingestion

---

## 14. Future Improvements
- Add feature store
- Introduce canary model deployment
- Monitor prediction distributions
