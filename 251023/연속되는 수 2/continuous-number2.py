n = int(input())
arr = [int(input()) for _ in range(n)]

count = 0
for i in range(n):
    if i == 0:
        count += 1
    elif arr[i] != arr[i-1]:
        count += 1

print(count)