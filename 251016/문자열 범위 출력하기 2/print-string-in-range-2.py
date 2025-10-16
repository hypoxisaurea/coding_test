sentence = input()
n = int(input())
length = len(sentence)

for i in range(n):
    print(sentence[length - i - 1], end='')