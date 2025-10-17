string = list(input())
length = len(string)
answer = ""

for i in range(length):
    if string[i] < 'A' or string[i] > 'z':
        continue
    else:
        answer += string[i]

print(answer.upper())