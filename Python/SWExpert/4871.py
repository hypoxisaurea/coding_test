T = int(input())

def dfs(node):
    if node == G:
        return 1
    
    visited[node] = True

    for next_node in graph[node]:
        if not visited[next_node]:
            if dfs(next_node) == 1:
                return 1
    
    return 0

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)

    S, G = map(int, input().split())
    visited = [False] * (V+1)

    answer = dfs(S)
    
    print(f'#{tc} {answer}')