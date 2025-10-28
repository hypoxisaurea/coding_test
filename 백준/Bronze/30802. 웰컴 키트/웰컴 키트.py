import sys

input = sys.stdin.readline

N = int(input())
applications = list(map(int, input().split()))
T, P = map(int, input().split())

t_shirts = 0
for count in applications:
    while count > 0:
        if count < T:
            t_shirts += 1
            break
        elif count >= T:
            t_shirts += (count // T)
            count %= T

pen_bundles = N // P
pen_individuals = N % P

print(t_shirts)
print(pen_bundles, pen_individuals)