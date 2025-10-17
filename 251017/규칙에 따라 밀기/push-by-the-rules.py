string = input()
command = list(input())
length = len(command)

for i in range(length):
    if command[i] == 'L':
        string = string[1:] + string[0]
    elif command[i] == 'R':
        string = string[-1] + string[0:len(string)-1]
    
print(string)