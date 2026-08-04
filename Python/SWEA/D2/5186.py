T = int(input())

for i in range(1, T+1):
    N = float(input())
    answer = ""

    while N > 0:
        N *= 2

        if N >= 1:
            answer += "1"
            N -= 1
        else:
            answer += "0"

        if len(answer) >= 13:
            break

    if len(answer) >= 13:
        print(f'#{i} overflow')
    else:
        print(f'#{i} {answer}')