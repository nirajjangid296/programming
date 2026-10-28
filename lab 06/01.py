for i in range(1,10):
    print("\t",i,end="")
print()
print("-"*40)
for i in range(1,10):
    print(i,end=" |\t")
    for j in range(1,10):
        print(i+j,"\t",end="")
    print()