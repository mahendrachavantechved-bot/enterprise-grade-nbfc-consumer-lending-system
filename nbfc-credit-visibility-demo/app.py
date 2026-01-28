import sys
import os

# ---- REQUIRED FOR NESTED STREAMLIT APPS ----
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

import streamlit as st
import json
from engine import run_credit_flow

st.set_page_config(page_title="NBFC Credit Risk Dashboard", layout="wide")
st.title("NBFC Credit Risk & Visibility Platform (2026)")

uploaded = st.file_uploader("Upload Applicant JSON", type=["json"])

if uploaded:
    applicant = json.load(uploaded)
else:
    with open(os.path.join(BASE_DIR, "data/sample_applicant.json")) as f:
        applicant = json.load(f)

if st.button("Run Credit Evaluation"):
    result = run_credit_flow(applicant)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Composite Score", result["composite_score"])
        st.write("Risk Band:", result["risk_band"]["label"])

    with col2:
        st.json(result)
