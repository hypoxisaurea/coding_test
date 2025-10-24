a = input()
length = len(a)
sum_val = 0


for i in range(length):
    if a[i].isdigit() == True:
        sum_val += int(a[i])


print(sum_val)