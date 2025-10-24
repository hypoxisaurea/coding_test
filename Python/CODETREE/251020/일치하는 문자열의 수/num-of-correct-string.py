n, A = input().split()
n = int(n)
count = 0

for i in range(n):
    string = input()

    if string == A:
        count += 1

print(count)