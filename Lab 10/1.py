numbers = tuple(map(int, input().split()))
value = int(input())

print(f"Tuple: {numbers}")
print(f"Length: {len(numbers)}")
print(f"Count of {value}: {numbers.count(value)}")
print(f"First index of {value}: {numbers.index(value) if value in numbers else (not in tuple)}")
