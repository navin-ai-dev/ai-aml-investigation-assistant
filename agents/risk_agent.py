# agents/risk_agent.py

def calculate_risk(df):

    score = 0

    if df["Amount"].max() > 100000:
        score += 40

    if len(df[df["Country"].isin(["Russia"])]) > 0:
        score += 30

    if len(df) > 5:
        score += 20

    return min(score, 100)