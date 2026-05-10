nums = []
rest = set()

for i in range(10):
    num = int(input())
    nums.append(num)

for i in nums:
    rest.add(i % 42)

print(len(rest))