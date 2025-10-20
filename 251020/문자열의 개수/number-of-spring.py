arr = []

while True:
    string = input()

    if string == '0':
        break

    arr.append(string)

print(len(arr))

for i in range(len(arr)):
    if i % 2 == 0:
        print(arr[i])