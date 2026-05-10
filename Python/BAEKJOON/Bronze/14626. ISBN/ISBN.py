ISBN = input()

not_check = ISBN[:-1]
result = int(ISBN[-1])
star_idx = -1

for i in range(len(not_check)):
    char = not_check[i]
    
    if char == '*':
        star_idx = i
        continue
        
    digit = int(char)
    
    if i % 2 == 0:
        result += (1 * digit)
    else:
        result += (3 * digit)
        
star_weight = 1 if star_idx % 2 == 0 else 3
total = 0

for i in range(0, 10):
    total = result + (star_weight * i)
    
    if total % 10 == 0:
        print(i)
        break