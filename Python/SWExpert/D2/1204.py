T = int(input())

for _ in range(T):
    tc = int(input())
    data = list(map(int, input().split()))

    score = [0] * 101

    for i in data:
        score[i] += 1

    max_count = max(score)
    answer = 0

    for i in range(100, -1, -1):
        if score[i] == max_count:
            answer = i
            break

    print(f'#{tc} {answer}')