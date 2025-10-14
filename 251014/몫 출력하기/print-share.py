count = 0

while True:
    try:
        if count >= 4:
            break

        n = int(input())

        if n % 2 == 1:
            continue
        else:
            print(n // 2)
            count += 1

    except EOFError:
        break