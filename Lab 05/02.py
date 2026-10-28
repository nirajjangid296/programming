n=int(input())
s=0
while n>0:
    a=n%10
    n=n//10
    s+=a
print(s)