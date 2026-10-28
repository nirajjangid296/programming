PRICE_PER_POUND = 2.50
pounds = float(input("Enter the number of pounds of apples: "))
cash = float(input("Enter the amount of cash tendered: $"))
total_cost = pounds * PRICE_PER_POUND
if cash >= total_cost:
    change = cash - total_cost
    print(f"Change: ${change:.2f}")
else:
    amount_owed = total_cost - cash
    print(f"You owe ${amount_owed:.2f} more.")