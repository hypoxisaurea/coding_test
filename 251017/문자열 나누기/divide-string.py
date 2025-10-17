n = int(input())
string = input().split()
sentence = ""

for i in range(len(string)):
    sentence += string[i]

for i in range(len(sentence)):
    print(sentence[i], end='')

    if (i + 1) % 5 == 0:
        print()