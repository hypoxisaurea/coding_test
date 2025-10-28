S = input()
a = ord('a')
z = ord('z')

result = []
for i in range(a, z + 1):
    character = chr(i)
    location = S.find(character)
    
    result.append(location)
    
print(*result)