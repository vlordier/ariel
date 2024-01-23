# Task Flow

Represents a flow of tasks in a project.

```mermaid
graph TD
Task1 -->|Task Link| Task2
Task2 ==>|Main Task| Task3
Task3 -.->|Side Task| Task4
Task4 -- Completion -- Finish
Finish -x
subgraph SG7 [Tasks Subgraph]
Task2 --> Task3
end
```
