apartment = [
    [0] * 15
    for _ in range(15)
]

for n in range(15):
    apartment[0][n] = n
    
for k in range(1, 15):
    for n in range(1, 15):
        apartment[k][n] = apartment[k][n-1] + apartment[k-1][n]

        
T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    
    print(apartment[k][n])