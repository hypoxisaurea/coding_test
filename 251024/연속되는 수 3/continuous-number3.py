N = int(input())
arr = [int(input()) for _ in range(N)]

count = 0
answer = 0

for i in range(N):
    if i >= 1 and arr[i - 1] * arr[i] > 0:
        count += 1
    else:
        count = 1

    answer = max(answer, count)

print(answer)