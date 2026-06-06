# agents/sar_agent.py

from langchain_groq import ChatGroq
import streamlit as st

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=st.secrets["GROQ_API_KEY"]
)

def generate_sar(
    risk_score,
    alerts,
    compliance,
    summary
):

    prompt = f"""
    Generate a Suspicious Activity Report (SAR).

    Risk Score:
    {risk_score}

    Alerts:
    {alerts}

    Compliance Findings:
    {compliance}

    Executive Summary:
    {summary}

    Include:

    1. Case ID
    2. Investigation Summary
    3. Suspicious Activities
    4. Risk Assessment
    5. Recommended Action
    6. Escalation Decision
    """

    return llm.invoke(prompt).content