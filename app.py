import streamlit as st

from utils.csv_reader import load_csv
from utils.dashboard import (
    transaction_country_chart,
    transaction_amount_chart
)
from utils.report_generator import generate_pdf

from agents.risk_agent import calculate_risk
from agents.pattern_agent import detect_patterns
from agents.compliance_agent import compliance_check
from agents.case_priority_agent import classify_case
from agents.investigation_agent import investigate_transactions
from agents.executive_summary_agent import generate_executive_summary
from agents.sar_agent import generate_sar

from utils.case_id_generator import (
    generate_case_id
)
from utils.case_manager import (
    save_case,
    get_cases,
    update_status
)
import plotly.express as px
st.set_page_config(
    page_title="AI AML Investigation Assistant",
    layout="wide"
)

st.title("🏦 AI AML Investigation Assistant")

st.markdown("""
AI-powered Anti Money Laundering Investigation Platform
for Risk, Compliance and Financial Crime Analysis.
""")

uploaded_file = st.file_uploader(
    "Upload Transaction CSV",
    type=["csv"]
)

if uploaded_file:

    # Load CSV
    df = load_csv(uploaded_file)

    st.success("CSV Uploaded Successfully")

    st.subheader("📄 Transaction Data")
    st.dataframe(df)

    # Analytics Dashboard
    st.subheader("📊 AML Analytics Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            transaction_country_chart(df),
            use_container_width=True
        )

    with col2:
        st.plotly_chart(
            transaction_amount_chart(df),
            use_container_width=True
        )

    # Risk Analysis
    risk_score = calculate_risk(df)

    alerts = detect_patterns(df)

    compliance = compliance_check(df)

    priority = classify_case(risk_score)
    case_id = generate_case_id()
    # KPI Section
    st.subheader("📈 Investigation Overview")

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:
        st.metric(
            "Risk Score",
            f"{risk_score}/100"
        )

    with kpi2:
        st.metric(
            "AML Alerts",
            len(alerts)
        )

    with kpi3:
        st.metric(
            "Compliance Flags",
            len(compliance)
        )

    with kpi4:
        st.metric(
            "Priority",
            priority
        )
   
    # Risk Status
    st.subheader("⚠️ Risk Assessment")

    if risk_score > 70:
        st.error("🔴 High Risk Customer")
    elif risk_score > 40:
        st.warning("🟠 Medium Risk Customer")
    else:
        st.success("🟢 Low Risk Customer")

    # AML Alerts
    st.subheader("🚨 AML Alerts")

    if alerts:
        for alert in alerts:
            st.error(alert)
    else:
        st.success("No AML Alerts Found")

    # Compliance Review
    st.subheader("📋 Compliance Review")

    if compliance:
        for item in compliance:
            st.warning(item)
    else:
        st.success("No Compliance Issues Found")

    st.subheader("🔍 AI Investigation Report")

    investigation_report = investigate_transactions(df)

    st.markdown(investigation_report)

    # Executive Summary
    st.subheader("📑 Executive AML Summary")

    summary = generate_executive_summary(
        risk_score,
        alerts,
        compliance
    )

    st.markdown(summary)
    st.subheader(
    "Case Management"
)

    if st.button(
        "Save Investigation Case"
    ):

        save_case(
    case_id,
    risk_score,
    priority,
    alerts,
    compliance,
    investigation_report,
    summary,
    ""
)

        st.success(
            f"{case_id} saved successfully"
        )
    # SAR Report
    st.subheader("📄 Suspicious Activity Report (SAR)")

    if st.button("Generate SAR Report"):

        sar_report = generate_sar(
            risk_score,
            alerts,
            compliance,
            summary
        )

        st.markdown(sar_report)

        pdf_file = generate_pdf(sar_report)

        with open(pdf_file, "rb") as file:

            st.download_button(
                label="📥 Download SAR Report",
                data=file,
                file_name=pdf_file,
                mime="application/pdf"
            )
    st.subheader(
    "Investigation Queue"
)

    cases = get_cases()

    st.dataframe(
        cases,
        use_container_width=True
    )
    st.subheader("⚙️ Update Case Status")

    cases = get_cases()

    if not cases.empty:

        selected_case = st.selectbox(
            "Select Case",
            cases["case_id"]
        )

        new_status = st.selectbox(
            "New Status",
            [
                "Open",
                "Investigating",
                "Escalated",
                "Closed"
            ]
        )

        if st.button("Update Status"):

            update_status(
                selected_case,
                new_status
            )

            st.success(
                "Status Updated"
            )

            st.rerun()
    st.subheader(
    "Priority Distribution"
)

    priority_chart = px.pie(
        cases,
        names="priority"
    )

    st.plotly_chart(
        priority_chart,
        use_container_width=True
    )
    st.subheader(
    "Case Status Distribution"
)

    status_chart = px.bar(
        cases.groupby("status")
        .size()
        .reset_index(name="Count"),
        x="status",
        y="Count"
    )

    st.plotly_chart(
        status_chart,
        use_container_width=True
    )