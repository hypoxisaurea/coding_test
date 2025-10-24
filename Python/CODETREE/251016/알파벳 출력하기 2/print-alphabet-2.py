n = int(input())
character = 65

for i in range(n):
    for j in range(i):
        print(' ', end=' ')
    
    for j in range(n-i):
        print(chr(character), end=' ')

        character += 1
        if chr(character) > 'Z':
            character = 65

    print()