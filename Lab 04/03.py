shape=input("enter the shape: ")
if shape=="square":
    a=int(input("length of its sides: "))
    area=a**2
elif shape=="rectangle":
    a=int(input("enter length of its side: "))
    b=int(input("enter length of other side: "))
    area=a*b
elif shape=="circle" :
    r=int(input("enter radius of the circle: "))
    area=3.14*r**2
else:
    a=int(input("enter base of the triangle: "))
    h=int(input("enter altitude of the triangle: "))
    area=1/2*a*h
print(f"{area:.3f}")