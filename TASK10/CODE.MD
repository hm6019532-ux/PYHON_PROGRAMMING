1. Problem Statement
Write a Python program to analyze student identification strings. Validate their structure, extract admission year, branch code, and student number, and classify students according to branch and admission year.


2. Algorithm
1. Start.
2. Read student identification number.
3. Check the ID length.
4. Validate the prefix.
5. Extract admission year.
6. Extract branch code.
7. Extract student number.
8. Classify the branch.
9. Display student details.
10. Stop.
3. Flowchart ---(Mermaid)
flowchart TD
    A([Start]) --> B[/Enter student ID/]
    B --> C{Valid ID format?}
    C -- No --> D[Display Invalid ID]
    C -- Yes --> E[Extract admission year]
    E --> F[Extract branch code]
    F --> G[Extract student number]
    G --> H{Identify branch}
    H --> I[Display student details]
    D --> J([Stop])
    I --> J
---
 



5. Sample Input
Enter student ID: NRI2026CSE001


6. Sample Output
Valid Student ID
Admission Year: 2026
Branch: Computer Science Engineering
Student Number: 001
