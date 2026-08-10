T = int(input())

for tc in range(1, T + 1):
    S = input().strip()
    balls = 0
    
    for i in range(len(S) - 1):
        if S[i] == '(' and (S[i+1] == '|' or S[i+1] == ')'):
            balls += 1
        elif S[i] == '|' and S[i+1] == ')':
            balls += 1
    
    print(f'#{tc} {balls}')