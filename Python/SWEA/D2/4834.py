T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().strip()))

    count = [0] * 10
    for card in cards:
        count[card] += 1

    max_num = 0
    max_count = 0

    for i in range(10):
        if count[i] >= max_count:
            max_num = i
            max_count = count[i]

    print(f'#{tc} {max_num} {max_count}')