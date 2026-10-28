n=int(input("number of elements"))
numbers=[]
for i in range(n):
    x=int(input("enter element"))
    numbers+=[x]
total=0
for i in range(len(numbers)):
    total+=numbers[i]
print(total)