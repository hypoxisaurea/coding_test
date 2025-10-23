OFFSET = 100
MAX_K = 201

N = int(input())
grid = [
    [0] * MAX_K
    for _ in range(MAX_K)
]
rects = [
    map(int, input().split())
    for _ in range(N)
]

for i, (x1, y1, x2, y2) in enumerate(rects):
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET

    if i % 2 == 0:
        for x in range(x1, x2):
            for y in range(y1, y2):
                grid[x][y] = 'R'
    else:
        for x in range(x1, x2):
            for y in range(y1, y2):
                grid[x][y] = 'B'


count = 0
for x in range(MAX_K):
    for y in range(MAX_K):
        if grid[x][y] == 'B':
            count += 1

print(count)