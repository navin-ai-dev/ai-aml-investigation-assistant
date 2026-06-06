import streamlit as st
from utils.case_manager import (
    get_cases,
    get_case
)

st.set_page_config(
    page_title="Case Details"
)

st.title("📂 AML Case Details")

cases = get_cases()

if cases.empty:
    st.warning("No cases found")
else:

    selected_case = st.selectbox(
        "Select Case",
        cases["case_id"]
    )

    case = get_case(selected_case)

    if case:

        st.subheader("📌 Case Information")

        st.write(
            f"**Case ID:** {case['case_id']}"
        )

        st.write(
            f"**Risk Score:** {case['risk_score']}"
        )

        st.write(
            f"**Priority:** {case['priority']}"
        )

        st.write(
            f"**Status:** {case['status']}"
        )

        st.write(
            f"**Investigator:** {case.get('investigator', 'Not Assigned')}"
        )

        st.write(
            f"**Created At:** {case['created_at']}"
        )

        st.subheader("🚨 AML Alerts")

        st.write(
            case.get("alerts", "No alerts found")
        )

        st.subheader("📋 Compliance Findings")

        st.write(
            case.get(
                "compliance",
                "No compliance findings"
            )
        )

        st.subheader("🔍 Investigation Report")

        st.write(
            case.get(
                "investigation_report",
                "No investigation report available"
            )
        )

        st.subheader("📑 Executive Summary")

        st.write(
            case.get(
                "executive_summary",
                "No executive summary available"
            )
        )

        st.subheader("📝 Investigator Notes")

        st.write(
            case.get(
                "notes",
                "No notes added"
            )
        )

        st.subheader("📄 SAR Report")

        st.write(
            case.get(
                "sar_report",
                "SAR report not generated"
            )
        )