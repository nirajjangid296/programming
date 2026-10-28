A=input("")
key=int(input(""))
encrypted=""
for i in A:
    encrypted+=chr(ord(i)+key)
print(encrypted)