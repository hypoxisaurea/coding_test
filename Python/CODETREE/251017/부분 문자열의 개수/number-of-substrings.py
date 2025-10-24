a = input()
b = input()

length = len(a)
count = 0

for i in range(length):
    if a[i] == b[0] and a[i+1] == b[1]:
        count += 1

print(count)