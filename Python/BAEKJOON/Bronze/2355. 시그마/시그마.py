A, B = map(int, input().split())

count = abs(A - B) + 1
pair_sum = A + B
answer = (pair_sum * count) // 2
    
print(answer)