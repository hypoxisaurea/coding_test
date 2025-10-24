n, k, t = input().split()
n, k = int(n), int(k)
strings = [input() for _ in range(n)]
result = []

for i in range(n):
    if strings[i].startswith(t):
        result.append(strings[i])

result.sort()
length = len(result)

print(result[k-1])