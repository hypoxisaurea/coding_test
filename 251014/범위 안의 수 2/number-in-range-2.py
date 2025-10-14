sum_val = 0
count = 0

for _ in range(10):
    num = int(input())

    if num >= 0 and num <= 200:
        count += 1
        sum_val += num

avg_val = sum_val / count
print(f"{sum_val} {avg_val:.1f}")