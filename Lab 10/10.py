def stats(nums):
    return min(nums), max(nums), sum(nums) / len(nums)


numbers = list(map(int, input().split()))
print(stats(numbers))
