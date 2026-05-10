import sys

T = int(sys.stdin.readline())
nums = []

for _ in range(T):
    num = int(sys.stdin.readline())
    nums.append(num)
    
nums.sort()

for num in nums:
    print(num)