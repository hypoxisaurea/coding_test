n = int(input())
arr = list(map(int, input().split()))
length = len(arr)

for i in range(1, n + 1):
    if i % 2 != 0:
        temp = arr[:i]
        temp.sort()
        median_val = temp[i // 2]
        
        print(median_val, end=' ')