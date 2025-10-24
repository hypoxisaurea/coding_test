letter = ord(input())
next_letter = chr(letter + 1)


if next_letter > 'z':
    next_letter = 'a'

print(next_letter)