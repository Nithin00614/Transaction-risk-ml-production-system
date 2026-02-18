import streamlit as st
import requests
import json

st.set_page_config(page_title="Transaction Risk Assessment", layout="wide")

st.title(" Transaction Risk Assessment")
st.markdown("Evaluate transaction risk in real-time using machine learning")

# API endpoint configuration
API_URL = "http://localhost:8000/score"

# Create two columns for layout
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📋 Transaction Details")
    
    amount = st.number_input(
        "Transaction Amount ($)",
        min_value=0.0,
        value=100.0,
        step=10.0,
        help="Amount of the transaction"
    )
    
    account_age_days = st.number_input(
        "Account Age (Days)",
        min_value=0,
        value=365,
        step=1,
        help="Number of days the account has been active"
    )
    
    past_txn_count_24h = st.number_input(
        "Transactions in Last 24h",
        min_value=0,
        value=3,
        step=1,
        help="Number of transactions in the past 24 hours"
    )
    
    hour_of_day = st.slider(
        "Hour of Day (24h format)",
        min_value=0,
        max_value=23,
        value=14,
        help="Hour when transaction occurred"
    )
    
    merchant_risk_score = st.slider(
        "Merchant Risk Score (0-1)",
        min_value=0.0,
        max_value=1.0,
        value=0.3,
        step=0.1,
        help="Risk score of the merchant"
    )

with col2:
    st.header(" Risk Assessment Results")
    
    if st.button("Analyze Transaction", key="analyze_btn", use_container_width=True):
        try:
            # Prepare request payload
            payload = {
                "amount": amount,
                "account_age_days": account_age_days,
                "past_txn_count_24h": past_txn_count_24h,
                "hour_of_day": hour_of_day,
                "merchant_risk_score": merchant_risk_score
            }
            
            # Make API request
            response = requests.post(API_URL, json=payload, timeout=5)
            response.raise_for_status()
            
            result = response.json()
            risk_score = result["risk_score"]
            decision = result["decision"]
            model_version = result["model_version"]
            
            # Display results with color coding
            st.success(" Assessment Complete")
            
            # Risk Score Gauge
            col_score, col_decision = st.columns(2)
            
            with col_score:
                st.metric(
                    label="Risk Score",
                    value=f"{risk_score:.2%}",
                    delta=None
                )
                st.progress(risk_score)
            
            with col_decision:
                if decision == "allow":
                    st.success(f"**Decision: {decision.upper()}** ✅")
                elif decision == "challenge":
                    st.warning(f"**Decision: {decision.upper()}** ⚠️")
                else:
                    st.error(f"**Decision: {decision.upper()}** ❌")
            
            # Risk Category
            if risk_score < 0.3:
                risk_category = "Low Risk"
                color = "🟢"
            elif risk_score < 0.7:
                risk_category = "Medium Risk"
                color = "🟡"
            else:
                risk_category = "High Risk"
                color = "🔴"
            
            st.info(f"{color} Risk Category: **{risk_category}**")
            st.caption(f"Model Version: {model_version}")
            
        except requests.exceptions.ConnectionError:
            st.error("❌ Cannot connect to API server. Make sure the FastAPI server is running on http://localhost:8000")
        except requests.exceptions.Timeout:
            st.error("❌ API request timed out. Try again.")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# Display scoring rules
with st.expander("📚 Scoring Rules"):
    st.markdown("""
    - **Allow** (Risk Score < 30%): Transaction is approved automatically
    - **Challenge** (Risk Score 30-70%): Additional verification may be required
    - **Block** (Risk Score > 70%): Transaction is blocked for security
    """)

# Footer
st.divider()
st.caption("Transaction Risk Assessment System v1.0")
