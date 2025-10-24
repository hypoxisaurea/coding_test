n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

def calc():
    global m
    answer = 0

    while m:
        answer += arr[m]
        
        if m % 2 == 1:
            m -= 1
        else:
            m //= 2

    return answer

print(calc())