x1=float(input("Enter x coordinate of the centre(x1): "))
y1=float(input("Enter y coordinate of the centre(y1): "))
r=float(input("Enter the radius of the cicle(r): "))
x2=float(input("Enter x coordinate of second point (x2): "))
y2=float(input("Enter y coordinate of second point (y2): "))
d=((x2-x1)**2+(y2-y1)**2)**1/2
if d==r:
    print("Second point is at the boundary of the circle")
elif d>r:
    print("Second point is outside the circle")
else:
    print("Second point is inside the circle")