n = int(input())
i = 1
sum_val = 0

while True:
    if n == i:
        break

    if n % i == 0:
        sum_val += i
    
    i += 1

if sum_val == n:
    print('P')
else:
    print('N')