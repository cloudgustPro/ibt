name = "kaleb"
balance = 864


def tier(balance):
    if balance >= 1000:
        return  "premium"
    elif balance >= 500:
        return  "basics"
    else:
        return "standard"

print(f"Customer: {name}")
print(f"balance: {balance} birr")
print(f"tier: {tier(balance)}")