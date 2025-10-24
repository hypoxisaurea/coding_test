start, end = map(int, input().split())
ans = 0

for i in range(start, end + 1):
    count = 0

    for j in range(1, i + 1):
        if i % j == 0:
            count += 1

    if count == 3:
        ans += 1

print(ans)