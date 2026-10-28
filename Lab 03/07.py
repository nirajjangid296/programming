i=int(input("enter 3 digit number "))

a=i//100
b=(i//10)%10
c=i%100

if i%(a+b+c)==0:
    print(i,"is a Harshad number")
else:
    print(i,"is not a Harshad number")