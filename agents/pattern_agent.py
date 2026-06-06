# agents/pattern_agent.py

def detect_patterns(df):

    alerts = []

    # Structuring Detection
    deposits = df[df["TransactionType"] == "Deposit"]

    if len(deposits) >= 3:
        avg_amount = deposits["Amount"].mean()

        if avg_amount > 40000:
            alerts.append(
                "🚨 Potential Structuring Detected"
            )

    # High Value Transfer

    if len(df[df["Amount"] > 100000]) > 0:
        alerts.append(
            "🚨 High Value Transfer Detected"
        )

    # High Risk Country

    high_risk = [
        "Russia",
        "Iran",
        "North Korea"
    ]

    if len(df[df["Country"].isin(high_risk)]) > 0:
        alerts.append(
            "🚨 High Risk Country Transfer"
        )

    return alerts