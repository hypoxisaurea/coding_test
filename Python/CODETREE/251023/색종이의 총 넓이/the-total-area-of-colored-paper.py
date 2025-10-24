OFFSET = 100
MAX_K = 201

n = int(input())
grid = [
    [0] * MAX_K
    for _ in range(MAX_K)
]

for _ in range(n):
    x1, y1 = map(int, input().split())
    x1, y1 = x1 + OFFSET, y1 + OFFSET

    x2, y2 = x1 + 8, y1 + 8

    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[i][j] += 1

count = 0
for i in range(MAX_K):
    for j in range(MAX_K):
        if grid[i][j] >= 1:
            count += 1

print(count)