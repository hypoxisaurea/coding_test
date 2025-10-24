sum_val = 0
count = 0

while True:
    n = int(input())

    if n // 10 != 2:
        break
    
    sum_val += n
    count += 1

avg_val = sum_val / count
print(f"{avg_val:.2f}")