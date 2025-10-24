sentence = input()
n = int(input())
length = len(sentence)
count = 0

for i in range(length - 1, -1 ,-1):
    if count >= n:
        break
    
    print(sentence[i], end='')
    count += 1