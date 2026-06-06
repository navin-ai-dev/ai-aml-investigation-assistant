import streamlit as st
import pandas as pd
import plotly.express as px
from utils.case_manager import (
    get_cases,
    update_status,
    update_case_details
)

from utils.sla_tracker import (
    calculate_case_age,
    get_sla_status
)

st.set_page_config(
    page_title="AML Manager Dashboard"
)

st.title("📊 AML Manager Dashboard")

cases = get_cases()

if not cases.empty:

    # ==========================
    # SLA DATA
    # ==========================

    sla_data = []

    for _, row in cases.iterrows():

        age = calculate_case_age(
            row["created_at"]
        )

        sla_status = get_sla_status(
            age,
            row["sla_days"]
        )

        sla_data.append(
            {
                "Case ID": row["case_id"],
                "Status": row["status"],
                "Age (Days)": age,
                "SLA Status": sla_status
            }
        )

    sla_df = pd.DataFrame(
        sla_data
    )

    # ==========================
    # KPI CALCULATIONS
    # ==========================

    total_cases = len(cases)

    open_cases = len(
        cases[
            cases["status"] == "Open"
        ]
    )

    investigating_cases = len(
        cases[
            cases["status"] == "Investigating"
        ]
    )

    escalated_cases = len(
        cases[
            cases["status"] == "Escalated"
        ]
    )

    breached_cases = len(
        sla_df[
            sla_df["SLA Status"]
            == "🔴 Breached"
        ]
    )
    critical_cases = len(
    cases[
        cases["priority"] == "Critical"
    ]
)

    high_risk_cases = len(
        cases[
            cases["risk_score"] >= 70
        ]
    )
    # ==========================
    # KPI DASHBOARD
    # ==========================

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            "Total Cases",
            total_cases
        )

    with col2:
        st.metric(
            "Open",
            open_cases
        )

    with col3:
        st.metric(
            "Investigating",
            investigating_cases
        )

    with col4:
        st.metric(
            "Escalated",
            escalated_cases
        )

    with col5:
        st.metric(
            "SLA Breached",
            breached_cases
        )
    st.subheader(
    "🚨 Escalation Dashboard"
)

    alert1, alert2, alert3, alert4 = st.columns(4)

    with alert1:
        st.error(
            f"Critical Cases: {critical_cases}"
        )

    with alert2:
        st.error(
            f"SLA Breached: {breached_cases}"
        )

    with alert3:
        st.warning(
            f"Escalated Cases: {escalated_cases}"
        )

    with alert4:
        st.warning(
            f"High Risk Cases: {high_risk_cases}"
        )
    st.subheader(
    "📈 Priority Distribution"
)

    priority_chart = px.bar(
        cases.groupby("priority")
        .size()
        .reset_index(name="Count"),
        x="priority",
        y="Count"
    )

    st.plotly_chart(
        priority_chart,
        use_container_width=True
    )
    st.subheader(
    "🔴 Critical Cases"
)

    critical_df = cases[
        cases["priority"] == "Critical"
    ]

    st.dataframe(
        critical_df,
        use_container_width=True
    )
    # ==========================
    # CASE QUEUE
    # ==========================

    st.subheader(
        "📂 Investigation Queue"
    )

    st.dataframe(
        cases,
        use_container_width=True
    )

    # ==========================
    # SLA MONITORING
    # ==========================

    st.subheader(
        "⏳ SLA Monitoring"
    )

    st.dataframe(
        sla_df,
        use_container_width=True
    )

    # ==========================
    # CASE STATUS UPDATE
    # ==========================

    st.subheader(
        "⚙️ Case Management"
    )

    selected_case = st.selectbox(
        "Select Case",
        cases["case_id"]
    )

    new_status = st.selectbox(
        "Update Status",
        [
            "Open",
            "Investigating",
            "Escalated",
            "Closed"
        ]
    )

    if st.button(
        "Update Status"
    ):

        update_status(
            selected_case,
            new_status
        )

        st.success(
            "Status Updated Successfully"
        )

        st.rerun()

    # ==========================
    # INVESTIGATOR ASSIGNMENT
    # ==========================

    st.subheader(
        "👨‍💼 Investigator Assignment"
    )

    investigator = st.selectbox(
        "Assign Investigator",
        [
            "John Smith",
            "Sarah Lee",
            "Michael Brown"
        ]
    )

    notes = st.text_area(
        "Investigator Notes"
    )

    if st.button(
        "Save Notes"
    ):

        update_case_details(
            selected_case,
            investigator,
            notes
        )

        st.success(
            "Case Updated Successfully"
        )

        st.rerun()

else:

    st.warning(
        "No AML Cases Found"
    )