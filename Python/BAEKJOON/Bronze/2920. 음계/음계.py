melody = list(map(int, input().split()))

count = 0
for i in range(7):
    if melody[i] < melody[i+1]:
        count += 1
    elif melody[i] > melody[i+1]:
        count -= 1

if count == 7:
    print('ascending')
elif count == -7:
    print('descending')
else:
    print('mixed')