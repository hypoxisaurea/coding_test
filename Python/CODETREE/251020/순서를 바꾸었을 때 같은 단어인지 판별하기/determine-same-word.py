word1 = list(input())
word2 = list(input())

word1.sort()
word2.sort()

length1 = len(word1)
length2 = len(word2)
different = False

if length1 != length2:
    different = True
else:
    for i in range(length1):
        if word1[i] == word2[i]:
            continue
        else:
            different = True

if different == False:
    print('Yes')
else:
    print('No')