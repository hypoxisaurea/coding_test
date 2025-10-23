OFFSET = 1000
MAX_K = 2001

n = 2
grid = [
    [0] * MAX_K
    for _ in range(MAX_K)
]
rects = [
    map(int, input().split())
    for _ in range(n)
]

for i, (x1, y1, x2, y2) in enumerate(rects, start = 1):
    x1 += OFFSET
    y1 += OFFSET

    x2 += OFFSET
    y2 += OFFSET

    for x in range(x1, x2):
        for y in range(y1, y2):
            grid[x][y] += i


count = 0
min_x, max_x = MAX_K, 0
min_y, max_y = MAX_K, 0

for x in range(MAX_K):
    for y in range(MAX_K):
        if grid[x][y] == 1:
            if max_x < x:
                max_x = x
            
            if min_x > x:
                min_x = x
            
            if max_y < y:
                max_y = y

            if min_y > y:
                min_y = y

if min_x == MAX_K:
    print(0)
else:
    print(((max_x - min_x) + 1) * ((max_y - min_y) + 1))