sentence, letter = input().split()

if letter in sentence:
    print(sentence.index(letter))
else:
    print('No')