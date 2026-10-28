w=int(input("kg"))
h=int(input("in m"))
bmi=w/(h**2)
if bmi<=18.5:
    print("underweight")
elif bmi<=25:
    print("normal weight")
elif bmi<=30:
    print("slightly over")    
elif bmi<=35:
    print("obese")
else:
    print("clinically obese")