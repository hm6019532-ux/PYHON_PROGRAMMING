
applicants = []

n = int(input("Enter number of applicants: "))

for i in range(n):
    print("\nApplicant", i + 1)

    app_id = input("Application ID: ")
    name = input("Name: ")
    aggregate = float(input("Aggregate marks (%): "))

    count = int(input("Number of subjects: "))
    subjects = []

    for j in range(count):
        mark = float(input(f"Subject {j + 1} marks: "))
        subjects.append(mark)

    attendance = float(input("Attendance (%): "))
    income = float(input("Annual family income: "))

    eligible = (
        aggregate >= 75
        and count > 0
        and all(mark >= 60 for mark in subjects)
        and attendance >= 75
        and income <= 250000
    )

    if eligible:
        applicants.append({
            "id": app_id,
            "name": name,
            "aggregate": aggregate,
            "min_subject": min(subjects),
            "attendance": attendance,
            "income": income
        })
        print("Status: Eligible")
    else:
        print("Status: Not Eligible")

# Ranking and tie-breaking rules
applicants.sort(key=lambda s: (
    -s["aggregate"],
    -s["min_subject"],
    -s["attendance"],
    s["income"],
    s["id"]
))

print("\n===== SCHOLARSHIP MERIT LIST =====")

if not applicants:
    print("No eligible applicants.")
else:
    for rank, s in enumerate(applicants, start=1):
        print(f"\nRank: {rank}")
        print("Application ID:", s["id"])
        print("Name:", s["name"])
        print("Aggregate:", s["aggregate"], "%")
        print("Minimum Subject Marks:", s["min_subject"], "%")
        print("Attendance:", s["attendance"], "%")
        print("Annual Income: Rs.", s["income"])

