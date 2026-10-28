n = int(input())
if n <= 0 or n % 2 == 0:
    print("Invalid input")
else:
    mid = n // 2
    for i in range(mid + 1):
        spaces = mid - i
        stars = 2 * i + 1
        for j in range(spaces):
            print(" ", end="")
        for j in range(stars):
            print("*", end="")
        print()
    for i in range(mid - 1, -1, -1):
        spaces = mid - i
        stars = 2 * i + 1
        for j in range(spaces):
            print(" ", end="")
        for j in range(stars):
            print("*", end="")
        print()