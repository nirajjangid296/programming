A=input("")
reverse=""
x=len(A)
for i in range(x-1,-1,-1):
    reverse+=A[i]
    
print(reverse)