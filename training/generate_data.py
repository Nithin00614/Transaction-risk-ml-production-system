import numpy as np
import pandas as pd

np.random.seed(42)

N = 100_000

data = {
    "amount": np.random.exponential(scale=2000, size=N),
    "account_age_days": np.random.randint(1, 2000, size=N),
    "past_txn_count_24h": np.random.poisson(2, size=N),
    "hour_of_day": np.random.randint(0, 24, size=N),
    "merchant_risk_score": np.random.uniform(0, 1, size=N),
}

df = pd.DataFrame(data)

# Fraud logic 
fraud_prob = (
    0.0005 * df["amount"] +
    0.003 * df["past_txn_count_24h"] +
    2.0 * df["merchant_risk_score"]
)

fraud_prob = np.clip(fraud_prob, 0, 1)
df["is_fraud"] = np.random.binomial(1, fraud_prob)

df.to_csv("data/raw/transactions.csv", index=False)

print("Synthetic dataset generated:", df.shape)
