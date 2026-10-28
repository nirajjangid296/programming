#problem 6
a=int(input("enter a "))
b=int(input("enter b "))
c=int(input("enter c "))

a=a+b+c
c=a-(b+c)
b=a-(b+c)
a=a-(b+c)
print(a)
print(b)
print(c)