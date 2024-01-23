
# Multi-Stage Process Flow

A Multi-Stage Process Flow is used to represent complex processes that are divided into distinct stages. Each stage consists of a series of steps or actions, and the transition between stages is often based on specific criteria or outcomes.

## Flow

```mermaid
graph TD
    subgraph SG1 [Stage 1: Preparation]
        A[Start] --> B[Step 1]
        B --> C[Step 2]
        C --> D[Step 3]
        D --> E[Transition to Stage 2]
    end
    subgraph SG2 [Stage 2: Execution]
        E --> F[Step 4]
        F --> G[Step 5]
        G --> H[Step 6]
        H --> I[Transition to Stage 3]
    end
    subgraph SG3 [Stage 3: Completion]
        I --> J[Step 7]
        J --> K[Step 8]
        K --> L[Step 9]
        L --> M[End]
    end
```
