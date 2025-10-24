m1, d1, m2, d2 = map(int, input().split())
A = input()

day_of_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

diff = sum(day_of_month[1:m2]) + d2 - (sum(day_of_month[1:m1]) + d1)
number = diff - day_of_week.index(A)

cnt = (number + 7) // 7

print(cnt)