
n = int(input("Enter number of transactions: "))

transactions = []

for i in range(n):
    tid = input("Enter transaction ID: ")
    amount = float(input("Enter amount: "))
    transactions.append((tid, amount))

threshold = float(input("Enter threshold amount: "))

ids = []
suspicious = []

for tid, amount in transactions:
    duplicate = tid in ids
    ids.append(tid)

    if duplicate or amount > threshold:
        suspicious.append((tid, amount))

print("\nSuspicious Transactions:")

for item in suspicious:
    print(item)

