while True:
    width, height, ch = input().split()

    width = int(width)
    height = int(height)

    print(width * height)

    if ch == 'C':
        break