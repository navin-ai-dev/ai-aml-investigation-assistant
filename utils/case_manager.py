import pandas as pd

from database import conn


def save_case(
    case_id,
    risk_score,
    priority,
    alerts,
    compliance,
    investigation_report,
    executive_summary,
    sar_report
):

    conn.execute(
        """
        INSERT INTO cases
        (
        case_id,
        risk_score,
        priority,
        status,
        alerts,
        compliance,
        investigation_report,
        executive_summary,
        sar_report,
        sla_days
        )
        VALUES
        
(
?,?,?,?,?,?,?,?,?,?
)
        """,
        (
    case_id,
    risk_score,
    priority,
    "Open",
    str(alerts),
    str(compliance),
    investigation_report,
    executive_summary,
    sar_report,
    3
)
    )

    conn.commit()


def get_cases():

    return pd.read_sql(
        "SELECT * FROM cases ORDER BY id DESC",
        conn
    )


def update_status(
    case_id,
    status
):

    conn.execute(
        """
        UPDATE cases
        SET status = ?
        WHERE case_id = ?
        """,
        (
            status,
            case_id
        )
    )

    conn.commit()

def update_case_details(
    case_id,
    investigator,
    notes
):

    conn.execute(
        """
        UPDATE cases
        SET investigator=?,
            notes=?
        WHERE case_id=?
        """,
        (
            investigator,
            notes,
            case_id
        )
    )

    conn.commit()
import sqlite3
from database import conn

def get_case(case_id):

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM cases
        WHERE case_id = ?
        """,
        (case_id,)
    )

    row = cursor.fetchone()

    if row:
        return dict(row)

    return None