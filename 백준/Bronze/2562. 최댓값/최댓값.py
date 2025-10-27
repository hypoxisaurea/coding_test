arr = []
for _ in range(9):
    num = int(input())
    arr.append(num)

max_val = arr[0]
max_idx = 0

for idx, num in enumerate(arr):
    if num > max_val:
        max_val = num
        max_idx = idx
        
print(max_val)
print(max_idx + 1)