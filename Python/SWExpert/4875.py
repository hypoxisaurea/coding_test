T = int(input())

for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input().strip())) for _ in range(N)]
    answer = 0
    
    start_x, start_y = 0, 0
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                start_x, start_y = i, j
    
    stack = [(start_x, start_y)]
    visited = [[False] * N for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while stack:
        x, y = stack.pop()

        if miro[x][y] == 3:
            answer = 1
            break
        
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and miro[nx][ny] != 1:
                    stack.append((nx, ny))

    print(f'#{tc} {answer}')