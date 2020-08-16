# [amount, [meals]]
bill = {}
total = 0
SALES_TAX = 0.235

def expense(meal, amount, name):
    if name in bill:
        bill[name][0] += amount
        bill[name][1].append(meal)
    else:
        bill[name] = [amount, [meal]]

    return amount

def split():
    for name in bill:
        amount = bill[name][0]
        print(f"{name}, ${amount} ({round(amount * 100 / total, 2)}%) - tax: ${round(amount * SALES_TAX, 2)}")
        for meal in bill[name][1]:
            print(f"- {meal}")

if __name__ == "__main__":
    total += expense("Katsu curry", 13.00, "Carlos")
    total += expense("Duck ramen", 15.50, "Wil")
    total += expense("Croquettes", 3.00, "Carlos")
    split()