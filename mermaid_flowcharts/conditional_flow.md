# Conditional Flow

Illustrates a process with a conditional decision-making step.

```mermaid
graph TD
Start -->|Start Process| Operation
Operation ==>|Important Step| Check
Check -.->|Condition?| Decision
Decision -- Normal Path -- NextStep
NextStep -o End
End -x Stop
subgraph SG2 [Decision Making]
Check --> Decision
end
```
