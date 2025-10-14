N = int(input())
digits_to_check = {'3', '6', '9'}

for i in range(1, N+1):
    if i % 3 == 0 or any(char in digits_to_check for char in str(i)):
        print(0, end=' ')
    else:
        print(i, end=' ')