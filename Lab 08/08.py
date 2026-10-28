string=input()
new=''
for i in string:
    if i not in new:
        new+=i
print(new)