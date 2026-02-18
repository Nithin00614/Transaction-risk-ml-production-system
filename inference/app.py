from fastapi import FastAPI
import numpy as np
from datetime import datetime

from inference.schemas import TransactionRequest, RiskResponse
from inference.model_loader import load_model

app = FastAPI(
    title="Transaction Risk Assessment API",
    description="ML-powered transaction risk scoring and decision engine",
    version="1.0.0"
)
model = load_model()


@app.get("/health")
def health_check():
    """Health check endpoint for monitoring and load balancing"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "model_loaded": model is not None
    }


@app.get("/metadata")
def get_metadata():
    """Retrieve API and model metadata"""
    return {
        "api_version": "1.0.0",
        "model_version": "logreg_v1",
        "model_type": "LogisticRegression",
        "features": [
            "amount",
            "account_age_days",
            "past_txn_count_24h",
            "hour_of_day",
            "merchant_risk_score"
        ],
        "decision_thresholds": {
            "allow": "< 0.3",
            "challenge": "0.3 - 0.7",
            "block": "> 0.7"
        },
        "last_updated": "2026-02-08"
    }


@app.post("/score", response_model=RiskResponse)
def score_transaction(req: TransactionRequest):
    """Score a transaction for fraud risk"""
    features = np.array([[
        req.amount,
        req.account_age_days,
        req.past_txn_count_24h,
        req.hour_of_day,
        req.merchant_risk_score
    ]])

    risk_score = model.predict_proba(features)[0][1]

    if risk_score < 0.3:
        decision = "allow"
    elif risk_score < 0.7:
        decision = "challenge"
    else:
        decision = "block"

    return RiskResponse(
        risk_score=risk_score,
        decision=decision,
        model_version="logreg_v1"
    )
