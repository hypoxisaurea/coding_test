string = list(input())
length = len(string)
answer = ""

first = string[0]
second = string[1]

for i in range(length):
    if string[i] == first:
        string[i] = second
    elif string[i] == second:
        string[i] = first

    answer += string[i]

print(answer)