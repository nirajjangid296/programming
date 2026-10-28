sen=input("").lower()
count=0
for i in range(97,123):
    i=chr(i)
    if i in sen:
        True
    else:
        count+=1
if count==0:
    print("pangram")
else:
    print("not a pangram")