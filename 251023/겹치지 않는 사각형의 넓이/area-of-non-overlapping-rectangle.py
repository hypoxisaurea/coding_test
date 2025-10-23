MAX_K = 2001
OFFSET = 1000

n = 3
rects = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
grid = [
    [0] * MAX_K
    for _ in range(MAX_K)
]

for i, (x1, y1, x2, y2) in enumerate(rects, start=1):
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET

    for x in range(x1, x2):
        for y in range(y1, y2):
            grid[x][y] += i

count = 0
for i in range(MAX_K):
    for j in range(MAX_K):
        if grid[i][j] == 1 or grid[i][j] == 2:
            count += 1

print(count)