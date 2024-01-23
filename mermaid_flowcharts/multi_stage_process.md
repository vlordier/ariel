# Multi-Stage Process

Describes a process divided into multiple stages.

```mermaid
graph TD
Start -->|First Stage| Middle
Middle ==>|Critical Stage| Last
Last -.->|Optional| OptionalEnd
OptionalEnd -- Final Step -- End
End -o Start
subgraph SG4 [Process Stages]
Middle --> Last
end
```
