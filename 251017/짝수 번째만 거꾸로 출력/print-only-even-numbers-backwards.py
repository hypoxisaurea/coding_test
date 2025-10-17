sentence = input()
selected = ""

for i in range(1, len(sentence), 2):
    selected += sentence[i]

print(selected[::-1])