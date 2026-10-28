n=int(input())
num=0
while n>0:
    r=n%8
    n=n//8
    num+=r*10
print(num)