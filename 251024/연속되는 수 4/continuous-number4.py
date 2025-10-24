n = int(input())
arr = [int(input()) for _ in range(n)]

count = 0
answer = 0

for i in range(n):
    if i > 0 and arr[i-1] < arr[i]:
        count += 1
    
    answer = max(answer, count)

print(answer)