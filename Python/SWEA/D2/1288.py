T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    
    answer = set()
    number = 0
    
    while len(answer) < 10:
        number += 1
        current = N * number
        
        for digit in str(current):
            answer.add(int(digit))
            
    print(f'#{tc} {current}')