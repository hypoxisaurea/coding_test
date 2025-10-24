n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

for i in range(m):
    a1 = queries[i][0]
    a2 = queries[i][1]
    sum_val = 0

    for j in range(a1-1, a2):
        sum_val += arr[j]

    print(sum_val)