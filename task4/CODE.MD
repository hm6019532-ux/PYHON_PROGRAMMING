1. Problem Statement
Write a Python program to generate a hollow diamond pattern based on user-specified dimensions. Validate invalid dimensions and display a properly aligned pattern.
2. Algorithm
1. Start.
2. Read the diamond size.
3. Check whether the size is positive.
4. Generate the upper half using a loop.
5. Generate the lower half using a reverse loop.
6. Display the hollow diamond.
7. Stop.
3. Flowchart 
..(Mermaid)
 
    A([Start]) --> B[/Enter diamond size/]
    B --> C{Size > 0?}
    C -- No --> D[Display Invalid Size]
    C -- Yes --> E[Generate upper half]
    E --> F[Generate lower half]
    F --> G[Display diamond]
    D --> H([Stop])
    G --> H
..
5. Sample Input
Enter diamond size: 4


6. Sample Output
   *
  * *
 *   *
*******
 *   *
  * *
   *
