# Hospital Admission Process

Detailed process of patient admission in a hospital.

```mermaid
graph TD
A[Patient Arrival] --> B[Initial Assessment]
B --> C[Registration]
C --> D[Insurance Verification]
D --> E[Medical History]
E --> F[Diagnosis]
F --> G[Treatment Planning]
G --> H[Bed Assignment]
H --> I[Patient Admission]
I --> J[Treatment Administration]
J --> K[Monitoring Patient]
K --> L[Ongoing Assessment]
L --> M[Family Communication]
M --> N[Care Coordination]
N --> O[Discharge Planning]
O --> P[Final Assessment]
P --> Q[Discharge Process]
Q --> R[Insurance Settlement]
R --> S[Patient Feedback]
S --> T[Post-Discharge Follow-Up]
subgraph Registration Phase
B --> C
C --> D
end
subgraph Treatment Phase
I --> J
J --> K
K --> L
end
subgraph Discharge Phase
O --> P
P --> Q
Q --> R
R --> S
end```
