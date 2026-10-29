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
Here is the University Scholarship Allocation Flowchart in Mermaid, line by line, with each step explained.

## Flowchart (Mermaid Code)

1. Start — Begin the program.
2. Enter number of applicants — Read how many students applied.
3. Enter applicant details — Read name, application ID, marks, attendance, and income.
4. Check aggregate marks — Are the marks at least 75%?
5. Check subject marks — Is every subject mark at least 60%?
6. Check attendance — Is attendance at least 75%?
7. Check income — Is annual family income ₹2,50,000 or less?
8. Store eligible applicant — Save the applicant if all conditions pass.
9. Mark applicant as ineligible — Reject the applicant if any condition fails.
10. Check for more applicants — If yes, repeat the input and eligibility checks.
11. Sort eligible applicants — Rank by aggregate marks, minimum subject marks, attendance, lower income, and application ID.
12. Display merit list — Print the final scholarship rankings.
13. Stop — End the program.
 
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

 
