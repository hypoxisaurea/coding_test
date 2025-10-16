words = []

for i in range(10):
    word = input()
    words.append(word)

letter = input()
count = 0

for i in range(10):
    if words[i][-1] == letter:
        count += 1
        print(words[i])
    
if count == 0:
    print('None')