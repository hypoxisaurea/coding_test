# 최대 이동 가능 거리 1000 * 100 = 100,000
# 좌우로 100,000씩 필요하므로 총 200,000 + 1 (0 포함)
MAX_K = 200001
# 배열의 중앙을 0번 인덱스로 사용하기 위한 오프셋
OFFSET = 100000

n = int(input())
# 현재 위치 (논리적 0번 타일)
curr = OFFSET

# 타일의 상태를 저장 (0: 회색, 1: 흰색, 2: 검은색)
arr = [0] * MAX_K

# 흰색, 검은색 타일 개수
white = 0
black = 0

for _ in range(n):
    x, direction = input().split()
    x = int(x)

    if direction == 'L':
        # 왼쪽으로 x칸 이동하며 칠하기
        for i in range(x):
            # --- 로직 수정 시작 ---
            
            # 현재 타일의 상태를 미리 확인
            is_white = (arr[curr] == 1)
            is_black = (arr[curr] == 2)

            # 1. 흰색으로 덮어쓸 때
            # 만약 이전에 검은색이었다면, 검은색 카운트 감소
            if is_black:
                black -= 1
            # 만약 이전에 흰색이 아니었다면 (회색 또는 검은색), 흰색 카운트 증가
            if not is_white:
                white += 1
            
            # 현재 타일을 흰색(1)으로 설정
            arr[curr] = 1
            
            # --- 로직 수정 끝 ---

            # 2. 위치 이동 (마지막 타일이 아닐 경우에만)
            if i < x - 1:
                curr -= 1
                
    else: # direction == 'R'
        # 오른쪽으로 x칸 이동하며 칠하기
        for i in range(x):
            # --- 로직 수정 시작 ---
            
            # 현재 타일의 상태를 미리 확인
            is_white = (arr[curr] == 1)
            is_black = (arr[curr] == 2)

            # 1. 검은색으로 덮어쓸 때
            # 만약 이전에 흰색이었다면, 흰색 카운트 감소
            if is_white:
                white -= 1
            # 만약 이전에 검은색이 아니었다면 (회색 또는 흰색), 검은색 카운트 증가
            if not is_black:
                black += 1
                
            # 현재 타일을 검은색(2)으로 설정
            arr[curr] = 2
            
            # --- 로직 수정 끝 ---
            
            # 2. 위치 이동 (마지막 타일이 아닐 경우에만)
            if i < x - 1:
                curr += 1

# 최종 흰색, 검은색 타일 수 출력
print(white, black)