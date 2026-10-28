n = int(input())
for num in range(1, n + 1):
    temp = num
    digits = 0
    while temp > 0:
        digits += 1
        temp //= 10
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10
    if total == num:
        print(num, end=" ")