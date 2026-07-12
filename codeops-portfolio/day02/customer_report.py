customers = [
    ("hiwot", 999),
    ("abebe", 1200),
    ("saba", 750),
    ("mulu", 400),
    ("hana", 200),
]


def tier(balance):
    if balance >= 1000:
        return "premium"
    elif balance >= 500:
        return "standard"
    else:
        return "basics"

premium = 0
standard = 0
basics = 0

print("Telebirr Customer Report")
print("------------------------")

for name, balance in customers:
    customer_tier = tier(balance)
    print(f"{name}: {customer_tier} ({balance} birr)")

    if customer_tier == "premium":
        premium += 1
    elif customer_tier == "standard":
        standard += 1
    else:
        basics += 1

print("\nCustomer Distribution:")
print(f"Premium: {premium}")
print(f"Standard: {standard}")
print(f"Basics: {basics}")