# Workflow Diagram

Demonstrates a typical workflow in an organization.

```mermaid
graph TD
Input -->|Process Input| Processing
Processing ==>|Main Processing| Output
Output -.->|Review| Review
Review -- Approval -- Completed
Completed -x
subgraph SG9 [Processing Steps]
Processing --> Output
end
```
