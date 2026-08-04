T = int(input())

for tc in range(1, T+1):
    str1 = input().strip()
    str2 = input().strip()

    N = len(str1)
    M = len(str2)

    answer = 0
    for start in range(M-N+1):
        if str2[start:start+N] == str1:
            answer = 1
            break

    print(f'#{tc} {answer}')