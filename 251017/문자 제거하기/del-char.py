string = list(input())

while True:
    if len(string) == 1:
        break

    index = int(input())

    if index >= len(string):
        string.pop(-1)
    else:
        string.pop(index)
    
    print(''.join(string))