import sys

input = sys.stdin.readline
N = int(input())

points = []
for i in range(N):
    x, y = map(int, input().split())
    points.append((x, y))
    
points.sort()
for x, y in points:
    print(x, y)