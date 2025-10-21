def dist(x, y):
    return abs(x) + abs(y)

n = int(input())
distance = []

for i in range(1, n+1):
    index = i
    x, y = tuple(map(int, input().split()))

    distance.append((dist(x, y), i))

distance.sort()

for _, index in distance:
    print(index)