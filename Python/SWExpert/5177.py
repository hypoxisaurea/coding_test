T = int(input())

def push(x):
    heap.append(x)
    idx = len(heap) - 1

    while idx > 1:
        parent = idx // 2

        if heap[parent] < heap[idx]:
            break

        heap[parent], heap[idx] = heap[idx], heap[parent]
        idx = parent

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    heap = [0]
    for x in data:
        push(x)

    answer = 0
    idx = N // 2

    while idx >= 1:
        answer += heap[idx]
        idx //= 2

    print(f'#{tc} {answer}')