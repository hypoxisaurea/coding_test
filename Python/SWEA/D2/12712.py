T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    plus_dr = [-1, 1, 0, 0]
    plus_dc = [0, 0, -1, 1]
    
    cross_dr = [-1, -1, 1, 1]
    cross_dc = [-1, 1, -1, 1]
    
    plus_sum = 0
    cross_sum = 0
    max_kill = 0
    
    for r in range(N):
        for c in range(N):
            plus_sum = grid[r][c]
            cross_sum = grid[r][c]
            
            for d in range(4):
                for k in range(1, M):
                    nr = r + plus_dr[d] * k
                    nc = c + plus_dc[d] * k
                    
                    if (0 <= nr < N) and (0 <= nc < N):
                        plus_sum += grid[nr][nc]
                        
            for d in range(4):
                for k in range(1, M):
                    nr = r + cross_dr[d] * k
                    nc = c + cross_dc[d] * k
                    
                    if (0 <= nr < N) and (0 <= nc < N):
                        cross_sum += grid[nr][nc]
    
                
            max_kill = max(max_kill, plus_sum, cross_sum)
            
    print(f'#{tc} {max_kill}')