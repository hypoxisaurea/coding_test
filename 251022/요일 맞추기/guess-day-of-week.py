def num_of_days(month, day):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0

    for i in range(1, month):
        total_days += days[i]

    total_days += day

    return total_days

m1, d1, m2, d2 = map(int, input().split())
day_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

diff = num_of_days(m2, d2) - num_of_days(m1, d1)

while diff < 0:
    diff += 7

print(day_of_week[diff % 7])