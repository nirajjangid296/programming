A=input().lower()
inverted=""
for i in range(len(A)-1,-1,-1):
    inverted+=A[i]
if inverted==A:
    print("palindrome")
else:
    print("not a palindrome")
    