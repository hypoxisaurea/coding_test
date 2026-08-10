T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    picture = [list(map(int, input().split())) for _ in range(N)]
    
    dr = [1, 0]
    dc = [0, 1]
    
    max_length = 0
    for r in range(N):
        length = 0
        
        for c in range(M):
            if picture[r][c] == 1:
                length += 1
                max_length = max(max_length, length)
            else:
                length = 0
                
    for c in range(M):
        length = 0
        for r in range(N):
            if picture[r][c] == 1:
                length += 1
                max_length = max(max_length, length)
            else:
                length = 0
        
    
    print(f'#{tc} {max_length}')