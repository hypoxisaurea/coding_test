T = int(input())

for tc in range(1, T+1):
    string = input().strip()
    stack = []
    answer = 1

    for ch in string:
        if ch == '(' or ch == '{':
            stack.append(ch)
        elif ch == ')':
            if not stack or stack[-1] != '(':
                answer = 0
                break

            stack.pop()
        elif ch == '}':
            if not stack or stack[-1] != '{':
                answer = 0
                break

            stack.pop()

    if stack:
        answer = 0

    print(f'#{tc} {answer}')