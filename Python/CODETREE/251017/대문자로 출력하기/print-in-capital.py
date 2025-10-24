string = list(input())
length = len(string)
answer = ""

for i in range(length):
    if (string[i] >= 'A' and string[i] <= 'Z') or (string[i] >= 'a' and string[i] <= 'z'):
        answer += string[i]
    else:
        continue

print(answer.upper())