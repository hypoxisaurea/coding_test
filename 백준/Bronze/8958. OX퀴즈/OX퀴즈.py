T = int(input())

for _ in range(T):
    result = input()
    score = 0
    count = 1
    
    for i in result:
        if i == 'O':
            score += count
            count += 1
        else:
            count = 1
            
    print(score)