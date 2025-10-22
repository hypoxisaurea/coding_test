m1, d1, m2, d2 = map(int, input().split())
A = input()

day_of_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']


def num_of_days(month, day):
    total_days = 0

    for i in range(1, month):
        total_days += day_of_month[i]
    
    total_days += day

    return total_days


diff = num_of_days(m2, d2) - num_of_days(m1, d1)
if diff < 0:
    diff += 7

today = diff % 7

count = 0
for i in range(diff + 1):
    if A == day_of_week[(today + i) % 7]:
        count += 1

print(count)