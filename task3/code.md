1. Problem Statement
Write a Python program to generate an examination seating arrangement using nested loops. Display row and column identifiers, reserved seats, and alternate seating restrictions.
2. Algorithm
1. Start.
2. Read the number of rows and columns.
3. Define reserved seating positions.
4. Use nested loops to generate seats.
5. Check whether a position is reserved.
6. Check alternate seating restrictions.
7. Display the seating arrangement.
8. Stop.
3. Flowchart
 ..(Mermaid)
 flowchart TD
    A([Start]) --> B[/Enter rows and columns/]
    B --> C[Initialize row loop]
    C --> D[Initialize column loop]
    D --> E{Reserved seat?}
    E -- Yes --> F[Display R]
    E -- No --> G{Alternate restriction?}
    G -- Yes --> H[Display X]
    G -- No --> I[Display S]
    F --> J[Next column]
    H --> J
    I --> J
    J --> K{More columns?}
    K -- Yes --> D
    K -- No --> L{More rows?}
    L -- Yes --> C
    L -- No --> M([Stop])
..
5. Sample Input
Enter number of rows: 4
Enter number of columns: 4


6. Sample Output
Row 1 : X R X S
Row 2 : S X S X
Row 3 : X S R S
Row 4 : S X S X
