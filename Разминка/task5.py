class AgeError(Exception):
    pass

class Person:
    def __init__(self, fio, age):
        if not 0 <= age <= 120:
            raise AgeError(f"возраст {age} за пределами 0..120")
        self.fio, self.age = fio, age

data = [("Белова Алина", 18), ("Орлов Максим", 130),
        ("Зайцев Никита", -1), ("Федорова Марина", 19)]
people = []
for name, years in data:
    try:
        people.append(Person(name, years))
    except AgeError as error:
        print(f"Не принято: {name} — {error}")
print("Принято:", len(people))
for person in people:
    print(person.fio, person.age)
