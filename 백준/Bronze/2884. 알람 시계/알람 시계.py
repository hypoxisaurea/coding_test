H, M = map(int, input().split())

if M >= 45:
    print(H, M-45)
else:
    H = H - 1
    M = 60 - abs(M - 45)
    
    if H < 0:
        H = 24 + H
        
    print(H, M)