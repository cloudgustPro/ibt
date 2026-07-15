customer_total = {}
try:
    with open("transaction.txt", "r") as file:
        for line in file:
            name, amount = line.strip().split(",")
            amount = float(amount)

            if name in customer_total:
                customer_total[name] += amount
            else:
                customer_total[name] = amount

    print("Customer Transaction Report")
    print("---------------------------")
    for name, total in customer_total.items():
        print(f"{name}: {total} birr")
except FileNotFoundError:
    print("Error: transaction.txt file not found.")