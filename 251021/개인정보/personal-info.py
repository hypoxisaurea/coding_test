class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def __str__(self):
        return f"{self.name} {self.height} {self.weight:.1f}"

n = 5
people = []

for _ in range(n):
    name, h, w = input().split()

    person = Person(name, int(h), float(w))
    people.append(person)

people.sort(key=lambda person : person.name)
print("name")
for i in range(n):
    print(people[i])

print()

people.sort(key=lambda person : -person.height)
print("height")
for i in range(n):
    print(people[i])