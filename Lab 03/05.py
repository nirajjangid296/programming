#problem 5
i=int(input("enter your digit: "))
a1=i%10
a2=(i%100)//10
a3=(i%1000)//100
a4=(i//10000)%10
a5=(i//10000)//10

if a1>=a2 and a1>=a3 and a1>=a4 and a1>=a5:
    print(a1,"1st position from left")
elif a2>=a3 and a2>a4 and a2>=a5:
    print(a2,"2nd position from left")
elif a3>=a4 and a3>=a5:
    print(a3,"3rd position from left")
elif a4>=a5:
    print(a4,"4th position from left")
else:
    print(a5,"5th position from left")