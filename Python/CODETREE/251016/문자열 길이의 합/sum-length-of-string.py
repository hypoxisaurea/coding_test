n = int(input())
sum_val = 0
count = 0

for _ in range(n):
    str_val = input()
    sum_val += len(str_val)

    if str_val[0] == 'a':
        count += 1


print(sum_val, count)