# agents/case_priority_agent.py

def classify_case(risk_score):

    if risk_score >= 80:
        return "🔴 Critical"

    elif risk_score >= 50:
        return "🟠 High"

    else:
        return "🟢 Low"