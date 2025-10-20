a, b = map(int, input().split())
sum_val = str(a + b)
count = 0

for i in range(len(sum_val)):
    if sum_val[i] == '1':
        count += 1

print(count)