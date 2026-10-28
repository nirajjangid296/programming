n=int(input("number of elements"))
numbers=[]
for i in range(n):
    x=int(input("enter element"))
    numbers+=[x]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]<numbers[j]:
            numbers[i],numbers[j]=numbers[j],numbers[i]
for i in range(len(numbers)):
    print(numbers[i],end=" ")