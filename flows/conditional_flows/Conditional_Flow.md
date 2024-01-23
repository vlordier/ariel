
# Conditional Flow

A Conditional Flow illustrates a process that involves decision-making steps leading to different outcomes or paths. It is particularly useful for mapping out processes where the next step depends on the result of a previous action.

## Flow

```mermaid
graph TD
    A[Start] --> B{Decision 1}
    B -->|Yes| C[Step 1 - Path A]
    C --> D{Decision 2}
    D -->|Yes| E[Step 2 - Path A]
    D -->|No| F[Step 2 - Path B]
    B -->|No| G[Step 1 - Path B]
    G --> H{Decision 3}
    H -->|Yes| I[Step 3 - Path A]
    H -->|No| J[Step 3 - Path B]
    E --> K[Step 4 - Path A]
    F --> L[Step 4 - Path B]
    I --> M[Step 5 - Path A]
    J --> N[Step 5 - Path B]
    K --> O[Step 6 - Path A]
    L --> P[Step 6 - Path B]
    M --> Q[Step 7 - Path A]
    N --> R[Step 7 - Path B]
    O --> S[Step 8 - Path A]
    P --> T[Step 8 - Path B]
    Q --> U[Step 9 - Path A]
    R --> V[Step 9 - Path B]
    S --> W[Step 10 - Path A]
    T --> X[Step 10 - Path B]
    U --> Y[Step 11 - Path A]
    V --> Z[Step 11 - Path B]
    W --> ZA[Step 12 - Path A]
    X --> ZB[Step 12 - Path B]
    Y --> ZC[Step 13 - Path A]
    Z --> ZD[Step 13 - Path B]
    ZA --> ZE[Step 14 - Path A]
    ZB --> ZF[Step 14 - Path B]
    ZC --> ZG[Step 15 - Path A]
    ZD --> ZH[Step 15 - Path B]
    ZE --> ZI[Step 16 - Path A]
    ZF --> ZJ[Step 16 - Path B]
    ZG --> ZK[Step 17 - Path A]
    ZH --> ZL[Step 17 - Path B]
    ZI --> ZM[Step 18 - Path A]
    ZJ --> ZN[Step 18 - Path B]
    ZK --> ZO[Step 19 - Path A]
    ZL --> ZP[Step 19 - Path B]
    ZM --> ZQ[Step 20 - Path A]
    ZN --> ZR[Step 20 - Path B]
    ZO --> ZS[End - Path A]
    ZP --> ZT[End - Path B]
    ZQ --> ZS
    ZR --> ZT
```
