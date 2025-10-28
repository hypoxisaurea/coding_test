T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    
    floor = (N - 1) % H + 1
    room_num = (N - 1) // H + 1
    final_room = (floor * 100) + room_num
    
    print(final_room)