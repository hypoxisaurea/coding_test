string = input()
length = len(string)
answer = ""

for i in range(length):
    if string[i].isalnum() == True:
        answer += string[i]
    else:
        continue

print(answer.lower())