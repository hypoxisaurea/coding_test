A = int(input())
B = int(input())
C = int(input())

target = str(A * B * C)
result = [0 for _ in range(10)]

for character in target:
    digit = int(character)
    result[digit] += 1
    
print(*result)