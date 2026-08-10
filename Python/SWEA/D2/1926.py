N = int(input())

for num in range(1, N + 1):
    clap = 0
    
    for digit in str(num):
        if digit in '369':
            clap += 1
            
    if clap > 0:
        print('-' * clap, end=' ')
    else:
        print(num, end=' ')