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
## 8. Decision Logic

The model outputs a probability score using Logistic Regression.

Based on this score, business decisions are applied:

- **risk_score < 0.3 → allow**
- **0.3 ≤ risk_score < 0.7 → challenge**
- **risk_score ≥ 0.7 → block**

This threshold-based decisioning simulates real-world fraud detection systems where model outputs are mapped to actionable outcomes.
---

## 9. API Design
POST /score

Request:
- Stateless JSON payload
- No user session dependency

Response:
- Risk score
- Decision label
- Model version

---

## 10. Scalability (Conceptual)
- Stateless service enables horizontal scaling
- Load balancer distributes traffic
- Each instance loads model once at startup
- No shared state between instances

---

## 11. Latency Considerations
- Simple model choice
- No database calls in inference path
- Minimal feature transformations
- Model loaded in memory

---

## 12. Failure Handling
- Invalid input rejected at schema validation
- Model load failure prevents service startup
- Timeouts handled at API gateway layer

---

## 13. Trade-offs
- Simpler model chosen over deep learning for reliability
- No real-time feature store to reduce latency
- Accuracy traded for predictability

---

## 14. Limitations
- No concept drift detection
- No online learning
- No streaming ingestion

---

## 15. Future Improvements
- Add feature store
- Introduce canary model deployment
- Monitor prediction distributions
