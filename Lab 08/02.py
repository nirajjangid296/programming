a=input()
output=''
for i in range(len(a)):
    if a[i].isalpha():
        if i%2==0:
            d=a[i]
            output+=d.upper()
        else:
            if a[i].isupper:
                d=a[i]
                output+=d.lower()
            else:
                output+=d
    else:
        output+=a[i]
print(output)