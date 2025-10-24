n, t = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
answer = 0

for i in range(n):
    if i > 0 and arr[i] > t:
        count += 1
    elif i == 0 and arr[i] > t:
        count = 1
    else:
        count = 0

    answer = max(count, answer)

print(answer)