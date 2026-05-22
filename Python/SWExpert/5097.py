from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    q = deque(map(int, input().split()))

    for _ in range(M):
        a = q.popleft()
        q.append(a)

    answer = q[0]


    print(f'#{tc} {answer}')