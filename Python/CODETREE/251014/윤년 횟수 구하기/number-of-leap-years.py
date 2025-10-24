N = int(input())
count = 0

for i in range(1, N+1):
    if i % 100 == 0 and i % 400 != 0:
        continue
    elif i % 4 == 0:
        count += 1

print(count)