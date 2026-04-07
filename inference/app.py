from fastapi import FastAPI
import numpy as np
import pandas as pd
from datetime import datetime
import warnings

from inference.schemas import TransactionRequest, RiskResponse
from inference.model_loader import load_model, FEATURE_NAMES

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
            "allow": "< 0.25",
            "challenge": "0.25 - 0.6",
            "block": "> 0.6"
        },
        "last_updated": "2026-02-08"
    }


@app.post("/score", response_model=RiskResponse)
def score_transaction(req: TransactionRequest):
    """Score a transaction for fraud risk"""
    # Create DataFrame with proper feature names and order
    features = pd.DataFrame([{
        "amount": req.amount,
        "account_age_days": req.account_age_days,
        "past_txn_count_24h": req.past_txn_count_24h,
        "hour_of_day": req.hour_of_day,
        "merchant_risk_score": req.merchant_risk_score
    }])
    
    # Ensure column order matches training
    features = features[FEATURE_NAMES]
    
    # Suppress feature name warnings during prediction
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=UserWarning)
        risk_score = model.predict_proba(features)[0][1]

    # Convert probability to business decision using thresholds
    if risk_score < 0.25:
        decision = "allow"
    elif risk_score < 0.6:
        decision = "challenge"
    else:
        decision = "block"

    return RiskResponse(
        risk_score=float(risk_score),
        decision=decision,
        model_version="logreg_v1"
    )
