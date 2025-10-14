n = int(input())

classroom = 0
hallway = 0
toilet = 0

for i in range(1, n+1):
    if i % 12 == 0:
        toilet += 1
    elif i % 2 == 0 and i % 3 == 0:
        hallway += 1
    elif i % 3 == 0:
        hallway += 1
    elif i % 2 == 0:
        classroom += 1

print(classroom, hallway, toilet)