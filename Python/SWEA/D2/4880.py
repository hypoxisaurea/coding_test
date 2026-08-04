T = int(input())

def fight(a, b):
    if cards[a] == cards[b]:
        return a

    if cards[a] == 1 and cards[b] == 3:
        return a
    if cards[a] == 2 and cards[b] == 1:
        return a
    if cards[a] == 3 and cards[b] == 2:
        return a

    return b


def winner(i, j):
    if i == j:
        return i

    mid = (i + j) // 2

    left = winner(i, mid)
    right = winner(mid + 1, j)

    return fight(left, right)


for tc in range(1, T+1):
    N = int(input())
    cards = [0] + list(map(int, input().split()))

    answer = winner(1, N)    

    print(f'#{tc} {answer}')