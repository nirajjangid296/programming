t=int(input("enter 4 digit number "))
a=t//1000
b=(t//100)%10
c=(t%100)//10
d=t%10

sum1=a+b
sum2=c+d
print(sum1)
print(sum2)

if sum1==sum2:
    print("equal")
else:
    print("not equal")