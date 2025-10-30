import sys

input = sys.stdin.readline

N = int(input())
arr = set(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

for num in targets:
    if num in arr:
        print(1)
    else:
        print(0)