A=input("")
word_length=0
for i in range(len(A)-1,-1,-1):
    if A[i]==" ":
        break
    else:
        word_length+=1
print(word_length)