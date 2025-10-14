satisfied = 0

for _ in range(5):
    n = int(input())

    if n % 3 == 0:
        satisfied += 1

if satisfied == 5:
    print(1)
else:
    print(0)