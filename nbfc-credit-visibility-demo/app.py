import streamlit as st
from engine import run_credit_flow

st.set_page_config(page_title="NBFC Credit Visibility Demo", layout="centered")

st.title("NBFC Credit Risk Dashboard")

result = run_credit_flow()

st.metric("Composite Risk Score", result["score"])
st.subheader("Risk Band")
st.markdown(
    f"<div style='padding:12px;background:{result['color']};color:white;border-radius:6px;'>"
    f"{result['label']}</div>",
    unsafe_allow_html=True
)
