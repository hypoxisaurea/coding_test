N = int(input())
numbers = int(input())

sum_val = 0
for i in range(N):
    sum_val += (numbers % 10)
    numbers //= 10

print(sum_val)