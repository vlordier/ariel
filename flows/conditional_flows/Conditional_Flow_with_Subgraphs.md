
# Conditional Flow with Subgraphs

A Conditional Flow with Subgraphs adds a layer of organization to a process involving decision-making steps and multiple paths. Subgraphs can help categorize different sections or types of decisions within the flow, making it easier to follow and understand.

## Flow

```mermaid
graph TD
    subgraph SG1 [Initial Decisions]
        A[Start] --> B{Decision 1}
        B -->|Yes| C[Step 1 - Path A]
        B -->|No| G[Step 1 - Path B]
    end
    subgraph SG2 [Path A]
        C --> D{Decision 2}
        D -->|Yes| E[Step 2 - Path A]
        D -->|No| F[Step 2 - Path B]
        E --> K[Step 4 - Path A]
        F --> L[Step 4 - Path B]
    end
    subgraph SG3 [Path B]
        G --> H{Decision 3}
        H -->|Yes| I[Step 3 - Path A]
        H -->|No| J[Step 3 - Path B]
        I --> M[Step 5 - Path A]
        J --> N[Step 5 - Path B]
    end
    subgraph SG4 [Further Steps in Path A]
        M --> Q[Step 7 - Path A]
        Q --> U[Step 9 - Path A]
        U --> Y[Step 11 - Path A]
        Y --> ZC[Step 13 - Path A]
        ZC --> ZG[Step 15 - Path A]
        ZG --> ZK[Step 17 - Path A]
        ZK --> ZM[Step 18 - Path A]
        ZM --> ZO[Step 19 - Path A]
        ZO --> ZQ[Step 20 - Path A]
        ZQ --> ZS[End - Path A]
    end
    subgraph SG5 [Further Steps in Path B]
        N --> R[Step 7 - Path B]
        R --> V[Step 9 - Path B]
        V --> Z[Step 11 - Path B]
        Z --> ZD[Step 13 - Path B]
        ZD --> ZH[Step 15 - Path B]
        ZH --> ZL[Step 17 - Path B]
        ZL --> ZN[Step 18 - Path B]
        ZN --> ZP[Step 19 - Path B]
        ZP --> ZR[Step 20 - Path B]
        ZR --> ZT[End - Path B]
    end
```
