from pydantic import BaseModel


class TransactionRequest(BaseModel):
    amount: float
    account_age_days: int
    past_txn_count_24h: int
    hour_of_day: int
    merchant_risk_score: float


class RiskResponse(BaseModel):
    risk_score: float
    decision: str
    model_version: str
