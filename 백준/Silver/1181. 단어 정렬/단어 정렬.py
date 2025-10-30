import sys

input = sys.stdin.readline

N = int(input())
words = set()
for _ in range(N):
    words.add(input().rstrip())
    
words = list(words)
words.sort(key=lambda x:(len(x), x))

for i in words:
    print(i)