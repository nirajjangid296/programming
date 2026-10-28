
costs = float(input("Enter the total costs: "))
revenue = float(input("Enter the total revenue: "))
if revenue == costs:
    print("Break even")
elif revenue > costs:
    print("Profit:", revenue - costs)
else:
    print("Loss:", costs - revenue)