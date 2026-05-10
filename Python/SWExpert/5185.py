T = int(input())

for i in range(1, T+1):
    N, hex_num = input().split()
    answer = ""

    for h in hex_num:
        answer += bin(int(h, 16))[2:].zfill(4)

    print(f'#{i} {answer}')