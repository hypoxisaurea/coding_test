sentence = input()
length = len(sentence)

count1 = 0
count2 = 0

for i in range(0, length-1):
    if sentence[i] == 'e' and sentence[i+1] == 'e':
        count1 += 1

    if sentence[i] == 'e' and sentence[i+1] == 'b':
        count2 += 1

print(count1, count2)