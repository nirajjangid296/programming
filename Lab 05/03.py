n=int(input())
dc=0
nc=0
while n!=-999:
    a=int(input())
    if a%n==0:
        dc+=1
    else:
        nc+=1
print(dc)
print(nc)