
student_id = input("Enter student ID: ").upper()

if (len(student_id) == 13 and
    student_id[:3] == "NRI" and
    student_id[3:7].isdigit() and
    student_id[7:10].isalpha() and
    student_id[10:13].isdigit()):

    year = student_id[3:7]
    branch = student_id[7:10]
    number = student_id[10:13]

    print("Valid Student ID")
    print("Admission Year:", year)

    if branch == "CSE":
        print("Branch: Computer Science Engineering")

    elif branch == "ECE":
        print("Branch: Electronics and Communication")

    elif branch == "EEE":
        print("Branch: Electrical Engineering")

    else:
        print("Branch: Other")

    print("Student Number:", number)

else:
    print("Invalid Student ID")

