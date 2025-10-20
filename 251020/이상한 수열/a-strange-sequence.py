N = int(input())

def calc(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    return calc(n // 3) + calc(n - 1)

print(calc(N))