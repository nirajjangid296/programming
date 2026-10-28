widgets = int(input("Enter the number of widgets ordered: "))
if widgets >= 100:
    price = 0.20
else:
    price = 0.25
total_cost = widgets * price
print("Total cost: ", format(total_cost, ".2f"))