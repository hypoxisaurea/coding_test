T = int(input())

for tc in range(1, T+1):
    str1 = input().strip()
    str2 = input().strip()

    max_count = 0

    for ch in str1:
        count = 0

        for s in str2:
            if ch == s:
                count += 1
        
        if count > max_count:
            max_count = count

    print(f'#{tc} {max_count}')