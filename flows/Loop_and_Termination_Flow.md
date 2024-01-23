
# Loop and Termination Flow

A Loop and Termination Flow is used to depict processes that involve repetitive actions and conditional terminations. It is ideal for illustrating cycles or iterations in a process, and how they conclude based on specific conditions.

## Flow

```mermaid
graph TD
    subgraph SG1 [Initialization]
        A[Start] --> B[Initialize Loop]
    end
    subgraph SG2 [Loop Process]
        B --> C{Check Condition}
        C -->|True| D[Perform Action]
        D --> B
    end
    subgraph SG3 [Termination]
        C -->|False| E[End Loop]
        E --> F[Finalize Process]
        F --> G[End]
    end
```
