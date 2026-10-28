sentence = input("Enter a sentence: ")
i = 0
capital = 0
small = 0
digit = 0
special = 0
while i < len(sentence):
    ch = sentence[i]
    if 'A' <= ch <= 'Z':
        capital += 1
    elif 'a' <= ch <= 'z':
        small += 1
    elif '0' <= ch <= '9':
        digit += 1
    else:
        special += 1
    i += 1
print("Capital letters =", capital)
print("Small letters =", small)
print("Digits =", digit)
print("Special characters =", special)