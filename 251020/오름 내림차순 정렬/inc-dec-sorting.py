n = int(input())
nums = list(map(int, input().split()))

a = sorted(nums)
b = sorted(nums, reverse=True)

for i in a:
    print(i, end=' ')

print()

for i in b:
    print(i, end=' ')