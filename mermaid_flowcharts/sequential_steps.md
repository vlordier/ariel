# Sequential Steps

A sequence of steps in a straightforward process.

```mermaid
graph TD
Step1 -->|Next| Step2
Step2 -- Path -- Step3
Step3 ==>|Priority| Step4
Step4 -.->|Optional| Step5
Step5 -x Finish
subgraph SG5 [Sequential Flow]
Step2 --> Step3
end
```
