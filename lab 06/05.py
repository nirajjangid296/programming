n = int(input())
first = int(input())
second = int(input())
if first > second:
    largest = first
    runner_up = second
else:
    largest = second
    runner_up = first
for i in range(n - 2):
    distance = int(input())
    if distance > largest:
        runner_up = largest
        largest = distance
    elif distance < largest and distance > runner_up:
        runner_up = distance
print(largest)
print(runner_up)