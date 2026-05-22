from collections import deque

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b]. append(a)
    
    S, G = map(int, input().split())

    visited = [0] * (V+1)
    q = deque()

    q.append(S)
    visited[S] = 1

    while q:
        now = q.popleft()

        for n_node in graph[now]:
            if visited[n_node] == 0:
                visited[n_node] = visited[now] + 1
                q.append(n_node)

    answer = visited[G] - 1 if visited[G] != 0 else 0

    print(f'#{tc} {answer}')