# Basic Process Flow

A simple demonstration of a basic process flow.

```mermaid
graph TD
A -->|Link Text| B
B -- Dotted Line -- C
C ==> E
E -.-> F
F -x G
G -o A
subgraph SG1 [Example Subgraph]
B --> C
end
```
