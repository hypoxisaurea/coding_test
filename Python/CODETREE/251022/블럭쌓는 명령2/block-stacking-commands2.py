n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

arr = [
    0 for _ in range(n + 1)
]

for a, b in commands:
    for i in range(a, b + 1):
        arr[i] += 1

print(max(arr))