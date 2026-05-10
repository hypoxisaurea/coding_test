T = int(input())

def binary_search_count(P, target):
    l = 1
    r = P
    count = 0

    while True:
        c = (l + r) // 2
        count += 1

        if c == target:
            return count

        elif target < c:
            r = c

        else:
            l = c

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    count_a = binary_search_count(P, Pa)
    count_b = binary_search_count(P, Pb)

    if count_a < count_b:
        winner = 'A'
    elif count_a > count_b:
        winner = 'B'
    else:
        winner = 0

    print(f'#{tc} {winner}')