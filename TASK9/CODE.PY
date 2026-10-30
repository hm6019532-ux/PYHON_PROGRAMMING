
record = input("Enter invoice record: ")

parts = record.split(",")

if len(parts) == 3:
    code = parts[0].strip()

    try:
        quantity = int(parts[1])
        amount = float(parts[2])

        if code and quantity > 0 and amount >= 0:
            print("Product Code:", code)
            print("Quantity:", quantity)
            print("Amount:", amount)
        else:
            print("Malformed Record")

    except ValueError:
        print("Malformed Record")

else:
    print("Malformed Record")

