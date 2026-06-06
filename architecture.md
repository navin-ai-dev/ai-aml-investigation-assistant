```mermaid
flowchart TD

A[Transaction CSV Upload]
--> B[Risk Scoring Engine]

B --> C[AML Pattern Detection]

C --> D[Compliance Review]

D --> E[AI Investigation Agent]

E --> F[Executive Summary Generator]

F --> G[SAR Generator]

G --> H[Case Management System]

H --> I[SQLite Database]

I --> J[Manager Dashboard]

J --> K[SLA Monitoring]

K --> L[Escalation Dashboard]

J --> M[Case Details Page]

J --> N[Investigator Assignment]
```
