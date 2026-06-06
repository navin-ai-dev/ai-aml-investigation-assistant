# agents/investigation_agent.py

from langchain_groq import ChatGroq
import streamlit as st

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=st.secrets["GROQ_API_KEY"]
)

def investigate_transactions(df):

    transactions = df.to_string()

    prompt = f"""
    You are an AML Investigator.

    Analyze these transactions.

    Identify:

    1. Suspicious transactions
    2. Money laundering indicators
    3. Risk level
    4. Recommendation

    Transactions:

    {transactions}
    """

    return llm.invoke(prompt).content