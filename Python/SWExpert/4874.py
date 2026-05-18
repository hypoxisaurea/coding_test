T = int(input())

for tc in range(1, T+1):
    s = list(input().split())
    nums = []
    error = False

    for ch in s:
        if ch == '.':
            break
        elif ch not in ['+', '-', '*', '/']:
            nums.append(int(ch))
        else:
            if len(nums) < 2:
                error = True
                break

            b = nums.pop()
            a = nums.pop()

            if ch == '+':
                nums.append(a+b)
            elif ch == '-':
                nums.append(a-b)
            elif ch == '*':
                nums.append(a*b)
            elif ch == '/':
                nums.append(a//b)

    if error or len(nums) != 1:
        print(f'#{tc} error')
    else:
        print(f'#{tc} {nums.pop()}')