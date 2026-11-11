"""Чтение, учёт и сохранение объектов анкет."""
from collections import Counter
from pathlib import Path
from people import AnketaError, Student, Teacher


def parse_line(text):
    fields = text.split(";")
    if len(fields) != 5:
        raise AnketaError(f"полей: {len(fields)}, ожидалось 5")
    kind, fio, email, phone, extra = fields
    kind = kind.strip().lower()
    if kind == "s":
        return Student(fio, email, phone, extra)
    if kind == "t":
        return Teacher(fio, email, phone, extra)
    raise AnketaError(f"неизвестный тип анкеты: {kind or '(пусто)'}")


class Registry:
    def __init__(self):
        self.people = []
        self.errors = []
        self.total = 0

    def add(self, person):
        self.people.append(person)

    def load(self, filename):
        try:
            source = Path(filename).read_text(encoding="utf-8").splitlines()
        except FileNotFoundError:
            return False
        self.people.clear()
        self.errors.clear()
        self.total = len(source)
        for number, line in enumerate(source, 1):
            if not line.strip():
                continue
            try:
                self.add(parse_line(line))
            except AnketaError as problem:
                self.errors.append((number, str(problem), line))
        return True

    def role_stats(self):
        return Counter(person.role() for person in self.people)

    def group_stats(self):
        result = Counter()
        for person in self.people:
            group = person.group_key()
            if group is not None:
                result[group] += 1
        return result

    def save_ok(self, filename):
        with Path(filename).open("w", encoding="utf-8") as output:
            for person in sorted(self.people):
                print(";".join((person.fio, person.email, person.phone,
                                person.role(), person.extra())), file=output)

    def save_errors(self, filename):
        with Path(filename).open("w", encoding="utf-8") as output:
            for num, reason, original in self.errors:
                print(f"Строка {num}: {reason}\n{original}", file=output)

    def __len__(self):
        return len(self.people)


if __name__ == "__main__":
    journal = Registry()
    print("Число анкет:", len(journal))
