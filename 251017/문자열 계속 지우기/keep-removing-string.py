A = input()
B = input()

len_A = len(A)
len_B = len(B)

while True:
    idx = -1
    candidates = len_A - len_B + 1

    for i in range(candidates):
        is_same = True
        
        for j in range(len_B):
            if A[i+j] != B[j]:
                is_same = False
                break

        if is_same:
            idx = i
            break

    if idx == -1:
        break

    A = A[:idx] + A[idx + len_B:]
    len_A = len(A)

print(A)