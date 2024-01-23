# Loop and Termination

Shows a loop process with a termination condition.

```mermaid
graph TD
Init -->|Initiate| Loop
Loop ==>|Repeat| Loop
Loop -.->|Exit Condition| Finish
Finish -- Path to End -- End
End -x
subgraph SG3 [Loop Process]
Loop --> Finish
end
```
