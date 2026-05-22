T = int(input())

def dfs(row, total):
    global answer

    if total >= answer:
        return
    
    if row == N:
        answer = min(answer, total)
        return
    
    for col in range(N):
        if not visited[col]:
            visited[col] = True
            dfs(row+1, total+arr[row][col])
            visited[col] = False

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    answer = 0

    dfs(0, 0)

    print(f'#{tc} {answer}')