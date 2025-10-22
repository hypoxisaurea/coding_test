n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

arr = [
    0 for _ in range(n)
]

for i in range(k):
    a, b = commands[i][0], commands[i][1]
    
    for j in range(a, b+1):
        arr[j] += 1

print(max(arr))