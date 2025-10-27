total = 0

for _ in range(4):
    total += int(input())

x = total // 60
y = total % 60

print(x)
print(y)