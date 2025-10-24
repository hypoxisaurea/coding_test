N = int(input())

def calc(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4
    else:
        return (calc(n-2) * calc(n-1)) % 100

print(calc(N))