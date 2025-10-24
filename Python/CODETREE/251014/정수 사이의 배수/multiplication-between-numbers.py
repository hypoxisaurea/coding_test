a, b = map(int, input().split())

sum_val = 0
count = 0

for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        sum_val += i
        count += 1

avg_val = sum_val / count

print(f"{sum_val} {avg_val:.1f}")
