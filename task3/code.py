
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

reserved = [(1, 2), (3, 3)]

for i in range(1, rows + 1):
    print("Row", i, ":", end=" ")

    for j in range(1, cols + 1):

        if (i, j) in reserved:
            print("R", end=" ")

        elif (i + j) % 2 == 0:
            print("X", end=" ")

        else:
            print("S", end=" ")

    print()

