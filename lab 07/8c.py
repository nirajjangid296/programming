n=int(input("number of elements"))
numbers=[]
for i in range(n):
    x=int(input("enter element"))
    numbers+=[x]
small=numbers[0]
for i in range(len(numbers)):
    if numbers[i]<small:
        small=numbers[i]
    else:
        continue
print(small)