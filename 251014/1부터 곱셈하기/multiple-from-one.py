n = int(input())
calc = 1

for i in range(1, 11):
    calc *= i

    if calc >= n:
        print(i)
        break