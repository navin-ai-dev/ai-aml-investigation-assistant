# database.py

import sqlite3

conn = sqlite3.connect(
    "aml_cases.db",
    check_same_thread=False
)

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS cases(

id INTEGER PRIMARY KEY AUTOINCREMENT,

case_id TEXT,

risk_score INTEGER,

priority TEXT,

status TEXT,

investigator TEXT,

notes TEXT,

alerts TEXT,

compliance TEXT,

investigation_report TEXT,

executive_summary TEXT,

sar_report TEXT,

sla_days INTEGER DEFAULT 3,

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

conn.commit()

try:
    cursor.execute(
        "ALTER TABLE cases ADD COLUMN investigator TEXT"
    )
except:
    pass

try:
    cursor.execute(
        "ALTER TABLE cases ADD COLUMN notes TEXT"
    )
except:
    pass

conn.commit()
try:
    cursor.execute(
        "ALTER TABLE cases ADD COLUMN sla_days INTEGER DEFAULT 3"
    )
except:
    pass

conn.commit()