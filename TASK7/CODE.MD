Problem Statement
Write a Python program to validate student email addresses and registration identifiers according to specified formatting rules. Identify malformed separators, invalid character groups, and missing components.
 Algorithm


1. Start.
2. Read student email and registration ID.
3. Check the email for @.
4. Check the email domain.
5. Validate the registration ID.
6. Check the ID prefix, year, branch, and number.
7. Display validation results.
8. Stop.


3. Flowchart ---(Mermaid)
 flowchart TD
    A([Start]) --> B[/Enter email and registration ID/]
    B --> C{Exactly one @?}
    C -- No --> D[Invalid Email]
    C -- Yes --> E{Valid email components?}
    E -- No --> D
    E -- Yes --> F[Valid Email]
    D --> G[Validate Registration ID]
    F --> G
    G --> H{Valid ID format?}
    H -- Yes --> I[Valid Registration ID]
    H -- No --> J[Invalid Registration ID]
    I --> K([Stop])
    J --> K
---


5. Sample Input
Enter student email: student@gmail.com
Enter registration ID: NRI2026CSE001


6. Sample Output
Valid Email
Valid Registration ID
