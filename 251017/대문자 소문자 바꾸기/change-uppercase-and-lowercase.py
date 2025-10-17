string = input()
length = len(string)
answer = ""

for i in range(length):
    if string[i].isupper() == True:
        answer += string[i].lower()
    else:
        answer += string[i].upper()

print(answer)