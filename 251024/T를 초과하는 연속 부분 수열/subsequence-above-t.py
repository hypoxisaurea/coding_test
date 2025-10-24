n, t = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
answer = 0

for i in range(n):
    if arr[i] > t:
        if i > 0:
            count += 1
        else:
            count = 1
    else:
        count = 1
        
    answer = max(answer, count)

print(count)