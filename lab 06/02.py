N=int(input())
for i in range(1,1001):
    if i%N==0 and i%4!=0:
        print(i,end=" ")