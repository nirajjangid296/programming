n=int(input())
d=0
for i in range(1,n+1):
    if n%i==0:
        d+=1
if d==2:
    print("prime")
else:
    print("not a prime")