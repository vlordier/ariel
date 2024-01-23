# Process Overview

An overview of a general process.

```mermaid
graph TD
Start -->|Begin| StepA
StepA -- Normal Flow -- StepB
StepB ==>|Critical Step| StepC
StepC -.->|Option| End
End -o Start
subgraph SG8 [Overview]
StepA --> StepB
end
```
