A=int(input("enter your angle "))
B=int(input("enter your angle "))
C=int(input("enter your angle "))
if A+B+C==180:
    if A==90 or B==90 or C==90:
        print("right angled triangle")
    elif A>90 or B>90 or C>90:
        print("acute angled triangle")
else:
    print("obtuse angled triangled")