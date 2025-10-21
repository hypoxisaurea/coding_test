class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

    def __str__(self):
        return f"{self.height} {self.weight} {self.number}"


n = int(input())
students = []

for i in range(1, n + 1):
    height, weight = tuple(map(int, input().split()))
    students.append(Student(height, weight, i))

students.sort(key=lambda x: (-x.height, -x.weight, x.number))

for student in students:
    print(student)