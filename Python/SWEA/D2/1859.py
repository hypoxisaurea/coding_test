T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))
    
    profit = 0
    max_price = prices[-1]
    
    for day in range(N - 2, -1, -1):
        if prices[day] > max_price:
            max_price = prices[day]
        else:
            profit += max_price - prices[day]
    
    print(f'#{tc} {profit}')