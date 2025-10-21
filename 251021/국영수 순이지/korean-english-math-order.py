n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def __str__(self):
        return f"{self.name} {self.kor} {self.eng} {self.math}"

students = []
for i in range(n):
    student = Student(name[i], korean[i], english[i], math[i])
    students.append(student)

students.sort(key=lambda student:(student.kor, student.eng, student.math), reverse=True)

for i in range(n):
    print(students[i])