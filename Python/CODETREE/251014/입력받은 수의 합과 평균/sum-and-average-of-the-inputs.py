N = int(input())

sum_val = 0

for _ in range(N):
    num = int(input())
    sum_val += num

avg_val = sum_val / N

print(f"{sum_val} {avg_val:.1f}")