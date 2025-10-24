n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

found = False
A.sort()
B.sort()

for i in range(n):
    if A[i] == B[i]:
        continue
    else:
        found = True

if found == True:
    print('No')
else:
    print('Yes')