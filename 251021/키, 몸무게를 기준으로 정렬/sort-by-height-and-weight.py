class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def __str__(self):
        return f"{self.name} {self.height} {self.weight}"


n = int(input())
people = []

for _ in range(n):
    n_i, h_i, w_i = input().split()

    person = Person(n_i, int(h_i), int(w_i))
    people.append(person)

people.sort(key=lambda person: (person.height, -person.weight))

for i in range(n):
    print(people[i])