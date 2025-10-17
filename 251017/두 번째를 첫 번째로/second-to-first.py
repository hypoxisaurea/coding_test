string = list(input())
length = len(string)

first = string[0]
second = string[1]


for i in range(length):
    if string[i] == second:
        string[i] = first

string = ''.join(string)

print(string)