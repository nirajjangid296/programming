sentence=input()
output=[]
for x in sentence:
    if x not in output:
        output.append(x)
print(output)