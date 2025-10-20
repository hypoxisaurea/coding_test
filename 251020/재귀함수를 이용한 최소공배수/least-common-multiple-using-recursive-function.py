n = int(input())
arr = list(map(int, input().split()))
ans = arr[0]

def gcd(a, b):
    if a < b:
        a, b = b, a

    if b == 0:
        return a

    return gcd(b, a % b)


def lcm(a, b):
    return int(a * b / gcd(a, b))

for num in arr:
    ans = lcm(num, ans)

print(ans)