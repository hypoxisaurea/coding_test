start, end = map(int, input().split())
count = 0

# Please write your code here.
for i in range(start, end + 1):
    sum_val = 0

    for j in range(1, i):
        if i % j == 0:
            sum_val += j
    
    if sum_val == i:
        count += 1

print(count)