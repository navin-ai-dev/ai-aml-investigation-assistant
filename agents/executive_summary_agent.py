# agents/executive_summary_agent.py

from langchain_groq import ChatGroq
import streamlit as st

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=st.secrets["GROQ_API_KEY"]
)

def generate_executive_summary(
    risk_score,
    alerts,
    compliance
):

    prompt = f"""
    Generate an AML Executive Summary.

    Risk Score:
    {risk_score}

    AML Alerts:
    {alerts}

    Compliance Findings:
    {compliance}

    Return:

    1. Executive Summary
    2. Key Risks
    3. Recommended Actions
    4. Escalation Decision
    """

    return llm.invoke(prompt).content