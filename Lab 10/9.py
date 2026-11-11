item_count = int(input())
stock = {}

for _ in range(item_count):
    item, quantity = input().split()
    stock[item] = int(quantity)

transaction_count = int(input())

for _ in range(transaction_count):
    action, item, quantity = input().split()
    quantity = int(quantity)

    if action == "SELL":
        if quantity > stock[item]:
            print(f"Insufficient stock: {item}")
        else:
            stock[item] -= quantity
    elif action == "ADD":
        stock[item] = stock.get(item, 0) + quantity

for item, quantity in stock.items():
    print(f"{item} {quantity}")
