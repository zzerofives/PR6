class Student:
    def __init__(self, fio, group):
        self.fio = " ".join(fio.split())
        self.group = group

    def short(self):
        words = self.fio.split()
        return words[0] + " " + " ".join(item[0] + "." for item in words[1:])

first = Student("Федорова Марина Викторовна", "09с41")
second = Student("Орлов Максим", "09с42")
first.group = "09с43"
print(first.short(), first.group)
print(second.short(), second.group)
