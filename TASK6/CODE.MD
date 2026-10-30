1. Problem Statement
Write a Python program to validate passwords using minimum length, uppercase letters, lowercase letters, digits, special characters, repetition, and prohibited substring rules. Display the failed conditions.
2. Algorithm
1. Start.
2. Read the password.
3. Check minimum length.
4. Check uppercase and lowercase letters.
5. Check digits and special characters.
6. Check consecutive repeated characters.
7. Check prohibited substring.
8. Display valid or invalid password.
9. Display failed conditions.
10. Stop.
3. Flowchart ---(Mermaid)
 flowchart TD
    A([Start]) --> B[/Enter password/]
    B --> C{Length >= 8?}
    C -- No --> D[Add length error]
    C -- Yes --> E[Check character categories]
    D --> E
    E --> F[Check repeated characters]
    F --> G[Check prohibited substring]
    G --> H{Errors present?}
    H -- Yes --> I[Display failed conditions]
    H -- No --> J[Display Valid Password]
    I --> K([Stop])
    J --> K
---


5. Sample Input
Enter password: Helo123@


6. Sample Output
Valid Password
