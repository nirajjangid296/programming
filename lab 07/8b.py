n=int(input("number of elements"))
numbers=[]
for i in range(n):
    x=int(input("enter element"))
    numbers+=[x]
product=1
for i in range(len(numbers)):
    product*=numbers[i]
print(product)