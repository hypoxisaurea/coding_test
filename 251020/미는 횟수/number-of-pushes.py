a = input()
b = input()

length = len(a)
count = 0
found = False

for i in range(length):
    a = a[-1] + a[:-1]
    count += 1

    if a == b:
        found = True
        print(count)

if found == False:
    print(-1)