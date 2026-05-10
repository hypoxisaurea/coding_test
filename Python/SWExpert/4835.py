T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    calc = []

    for start in range(N - M + 1):
        total = 0

        for i in range(start, start + M):
            total += arr[i]
        
        calc.append(total)

    answer = max(calc) - min(calc)
    print(f'#{tc} {answer}')