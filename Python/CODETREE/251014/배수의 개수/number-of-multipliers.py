count_3 = 0
count_5 = 0

for _ in range(10):
    num = int(input())

    if num % 3 == 0 and num % 5 == 0:
        count_3 += 1
        count_5 += 1
    elif num % 3 == 0:
        count_3 += 1
    elif num % 5 == 0:
        count_5 += 1

print(count_3, count_5)