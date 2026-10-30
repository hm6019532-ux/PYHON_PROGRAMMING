1. Problem Statement
Write a Python program to process transaction IDs and amounts. Detect duplicate transactions, identify transactions exceeding a specified threshold, and generate a list of suspicious transactions.
2. Algorithm
1. Start.
2. Read the number of transactions.
3. Read transaction ID and amount.
4. Store transactions in a list.
5. Read the amount threshold.
6. Check duplicate transaction IDs.
7. Check amount threshold violations.
8. Display suspicious transactions.
9. Stop.
3. Flowchart
---mermaid
flowchart TD
    A([Start]) --> B[/Enter number of transactions/]
    B --> C[/Enter transaction ID and amount/]
    C --> D[Store in list]
    D --> E{More transactions?}
    E -- Yes --> C
    E -- No --> F[/Enter threshold/]
    F --> G[Check duplicate IDs]
    G --> H{Duplicate or amount above threshold?}
    H -- Yes --> I[Add to suspicious list]
    H -- No --> J[Normal transaction]
    I --> K{More transactions?}
    J --> K
    K -- Yes --> G
    K -- No --> L[Display suspicious list]
    L --> M([Stop])
---

5. Sample Input
Enter number of transactions: 3
Enter transaction ID: T101
Enter amount: 500
Enter transaction ID: T102
Enter amount: 9000
Enter transaction ID: T101
Enter amount: 300
Enter threshold amount: 5000


6. Sample Output
Suspicious Transactions:
('T102', 9000.0)
('T101', 300.0)
