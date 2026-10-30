
email = input("Enter student email: ")
reg = input("Enter registration ID: ")

# Email validation
if email.count("@") == 1:
    parts = email.split("@")

    if (parts[0] and "." in parts[1]
        and not parts[1].startswith(".")
        and not parts[1].endswith(".")
        and " " not in email):
        print("Valid Email")
    else:
        print("Invalid Email")
else:
    print("Invalid Email")

# Registration ID validation
if (len(reg) == 13 and
    reg[:3] == "NRI" and
    reg[3:7].isdigit() and
    reg[7:10].isalpha() and
    reg[10:13].isdigit()):

    print("Valid Registration ID")
else:
    print("Invalid Registration ID")

