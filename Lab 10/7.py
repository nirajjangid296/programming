numbers = tuple(map(int, input().split()))
even_numbers = tuple(i for i in numbers if i % 2 == 0)
print(even_numbers)
