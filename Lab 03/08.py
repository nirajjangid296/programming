#problem 8
V=float(input("enter initil aquantity of water "))
N=int(input("no of days "))
f=(V*(0.95**N))+200*(1-(0.95**N))
print(f)