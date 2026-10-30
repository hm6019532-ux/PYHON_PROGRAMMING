1. Problem Statement
Write a Python program to calculate water bills for multiple households using consumption slabs, fixed fees, and penalties. Compare consumption and identify excessive water usage.
2. Algorithm
1. Start.
2. Read the number of households.
3. Read household name and water consumption.
4. Calculate charges using consumption slabs.
5. Add fixed fee.
6. Apply penalty for excessive usage.
7. Display the total bill.
8. Identify households with excessive usage.
9. Stop.
3. Flowchart 
..(Mermaid)
 
 flowchart TD
    A([Start]) --> B[/Enter number of households/]
    B --> C[/Enter name and consumption/]
    C --> D{Consumption <= 100?}
    D -- Yes --> E[Calculate at Rs. 2 per unit]
    D -- No --> F{Consumption <= 200?}
    F -- Yes --> G[Calculate first 100 at Rs. 2 and rest at Rs. 3]
    F -- No --> H[Calculate remaining units at Rs. 5]
    E --> I[Add fixed fee]
    G --> I
    H --> I
    I --> J{Consumption > 300?}
    J -- Yes --> K[Add penalty]
    J -- No --> L[Display bill]
    K --> L
    L --> M{More households?}
    M -- Yes --> C
    M -- No --> N([Stop])
..


5. Sample Input
Enter number of households: 2
Enter household name: Ravi
Enter water consumption: 80
Enter household name: Kumar
Enter water consumption: 350


6. Sample Output
Household: Ravi
Total Bill: Rs. 210
Normal Usage

Household: Kumar
Total Bill: Rs. 1200
Excessive Usage
