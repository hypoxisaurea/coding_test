T = int(input())

for i in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_num = max(arr)
    min_num = min(arr)

    print(f'#{i} {max_num - min_num}')