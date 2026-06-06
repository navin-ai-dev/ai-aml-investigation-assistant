# utils/dashboard.py

import plotly.express as px


def transaction_country_chart(df):

    chart = px.bar(
        df.groupby("Country")
        .size()
        .reset_index(name="Transactions"),
        x="Country",
        y="Transactions",
        title="Transactions by Country"
    )

    return chart


def transaction_amount_chart(df):

    chart = px.pie(
        df,
        names="Country",
        values="Amount",
        title="Transaction Amount Distribution"
    )

    return chart