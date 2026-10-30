1. Problem Statement
Write a Python program to compare student answers with an answer key. Calculate correct, incorrect, and unanswered responses, apply negative marking, and display the final examination score.


2. Algorithm
1. Start.
2. Read the answer key.
3. Read student answers.
4. Check whether both strings have equal lengths.
5. Compare answers character by character.
6. Count correct answers.
7. Count incorrect answers.
8. Count unanswered questions.
9. Calculate final marks.
10. Display the result.
11. Stop.


3. Flowchart ---(Mermaid)
 flowchart TD
    A([Start]) --> B[/Enter answer key/]
    B --> C[/Enter student answers/]
    C --> D{Equal length?}
    D -- No --> E[Display Invalid Answers]
    D -- Yes --> F[Initialize counters]
    F --> G[Compare each answer]
    G --> H{Answer is -?}
    H -- Yes --> I[Count unanswered]
    H -- No --> J{Answer correct?}
    J -- Yes --> K[Count correct]
    J -- No --> L[Count incorrect]
    I --> M{More answers?}
    K --> M
    L --> M
    M -- Yes --> G
    M -- No --> N[Calculate score]
    N --> O[Display result]
    E --> P([Stop])
    O --> P
---



5. Sample Input
Enter answer key: ABCDA
Enter student answers: ABCCA


6. Sample Output
Correct: 4
Incorrect: 1
Unanswered: 0
Final Score: 15
