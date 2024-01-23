# Decision-Making Flow

Focuses on a decision-making process with multiple options.

```mermaid
graph TD
Decide -->|Choose Path| Option1
Option1 ==>|Preferred| Option2
Option2 -.->|Alternative| Option3
Option3 -- Link -- End
End -o Restart
subgraph SG6 [Decisions]
Decide --> Option1
end
```
