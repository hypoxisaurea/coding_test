n = int(input())
words = []

for i in range(n):
    word = input()
    words.append(word)

letter = input()
count = 0
sum_val = 0

for i in range(n):
    if words[i][0] == letter:
        count += 1
        sum_val += len(words[i])

print(f"{count} {sum_val/count:.2f}")