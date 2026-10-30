# University Scholarship Allocation System

## 1. Problem Statement

 University Scholarship Allocation: Design a system that evaluates applicants using aggregate marks, subject-wise minimum scores, attendance, and income criteria, ranks eligible students, and resolves ties using predefined rules
## 2. Algorithm

1. Start the program.
2. Read the number of applicants.
3. For each applicant, input application ID, name, aggregate marks, subject-wise marks, attendance, and annual family income.
4. Check the eligibility criteria:
   - Aggregate marks ≥ 75%.
   - Every subject mark ≥ 60%.
   - Attendance ≥ 75%.
   - Annual family income ≤ ₹2,50,000.
5. Store eligible applicants and display the rejection status for ineligible applicants.
6. Sort eligible applicants using the following tie-breaking priorities:
   - Higher aggregate marks.
   - Higher minimum subject marks.
   - Higher attendance.
   - Lower family income.
   - Application ID in ascending order.
7. Display the ranked scholarship merit list.
8. Stop.

 ##FLOW CHART
---mermaid 
flowchart TD
    A([Start])
    B[/Enter number of applicants/]
    C[/Enter applicant details/]
    D{Aggregate marks >= 75%?}
    E{All subject marks >= 60%?}
    F{Attendance >= 75%?}
    G{Annual income <= 250000?}
    H[Store applicant as eligible]
    I[Mark applicant as ineligible]
    J{More applicants?}
    K[Sort eligible applicants by merit and tie-break rules]
    L[/Display scholarship merit list/]
    M([Stop])
---
    A --> B
    B --> C
    C --> D
    D -- Yes --> E
    D -- No --> I
    E -- Yes --> F
    E -- No --> I
    F -- Yes --> G
    F -- No --> I
    G -- Yes --> H
    G -- No --> I
    H --> J
    I --> J
    J -- Yes --> C
    J -- No --> K
    K --> L
    L --> M

 
## 5. Sample Input

```
Enter number of applicants: 3

Applicant 1
Application ID: A003
Name: Ravi
Aggregate marks (%): 92
Number of subjects: 3
Subject 1 marks: 90
Subject 2 marks: 95
Subject 3 marks: 91
Attendance (%): 90
Annual family income: 180000

Applicant 2
Application ID: A001
Name: Priya
Aggregate marks (%): 85
Number of subjects: 3
Subject 1 marks: 80
Subject 2 marks: 85
Subject 3 marks: 90
Attendance (%): 88
Annual family income: 200000

Applicant 3
Application ID: A002
Name: Kiran
Aggregate marks (%): 70
Number of subjects: 3
Subject 1 marks: 75
Subject 2 marks: 80
Subject 3 marks: 70
Attendance (%): 90
Annual family income: 150000
```

## 6. Sample Output

```
Status: Eligible
Status: Eligible
Status: Not Eligible

===== SCHOLARSHIP MERIT LIST =====

Rank: 1
Application ID: A003
Name: Ravi
Aggregate: 92.0 %
Minimum Subject Marks: 90.0 %
Attendance: 90.0 %
Annual Income: Rs. 180000.0

Rank: 2
Application ID: A001
Name: Priya
Aggregate: 85.0 %
Minimum Subject Marks: 80.0 %
Attendance: 88.0 %
Annual Income: Rs. 200000.0
```

 
