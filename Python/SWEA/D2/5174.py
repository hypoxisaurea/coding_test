T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))

    graph = [[] for _ in range(E+2)]

    for i in range(0, len(data), 2):
        parent = data[i]
        child = data[i+1]
        
        graph[parent].append(child)

    count = 0
    stack = [N]

    while stack:
        node = stack.pop()
        count += 1

        for child in graph[node]:
            stack.append(child)
        
    print(f'#{tc} {count}')