
password = input("Enter password: ")

errors = []

if len(password) < 8:
    errors.append("Minimum 8 characters required")

if not any(c.isupper() for c in password):
    errors.append("Uppercase letter missing")

if not any(c.islower() for c in password):
    errors.append("Lowercase letter missing")

if not any(c.isdigit() for c in password):
    errors.append("Digit missing")

if not any(not c.isalnum() for c in password):
    errors.append("Special character missing")

for i in range(len(password) - 1):
    if password[i] == password[i + 1]:
        errors.append("Repeated consecutive characters")
        break

if "password" in password.lower():
    errors.append("Prohibited substring found")

if errors:
    print("Invalid Password")
    for error in errors:
        print(error)
else:
    print("Valid Password")

