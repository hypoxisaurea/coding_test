T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    answer = ""

    for _ in range(N):
        arr.append(input().strip())

    for row in range(N):
        for start in range(N-M+1):
            word = arr[row][start:start+M]
        
            if word == word[::-1]:
                answer = word
                break

        if answer:
            break

    if not answer:
        for col in range(N):
            for start in range(N-M+1):
                word = ""
                for row in range(start, start + M):
                    word += arr[row][col]
                
                if word == word[::-1]:
                    answer = word
                    break
            
            if answer:
                break
            

    print(f'#{tc} {answer}')