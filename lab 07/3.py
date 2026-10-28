sen=input("").lower()
word=input("").lower()

count=0
for i in range(len(sen)-len(word)+1):
    for j in range(len(word)):
        if sen[i+j]!=word[j]:
            False
            break
    else:
        count+=1
if count>0:
    print("word is present",count)
else:
    print("not present")
    