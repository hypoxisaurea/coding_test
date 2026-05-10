T = int(input())

for tc in range(1, T+1):
    N = int(input())
    area = [[0] * 10 for _ in range(10)]

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for row in range(r1, r2+1):
            for col in range(c1, c2+1):
                if area[row][col] == 0:
                    area[row][col] = color
                else:
                    if area[row][col] == color:
                        continue
                    else:
                        area[row][col] = 9
            
    answer = 0
    for i in range(10):
        for j in range(10):
            if area[i][j] == 9:
                answer += 1

    print(f'#{tc} {answer}')