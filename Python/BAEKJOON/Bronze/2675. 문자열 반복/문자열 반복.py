T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)
    P = ""
    
    for word in S:
        P += (word * R)
    
    print(P)