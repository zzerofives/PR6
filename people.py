"""Общие свойства анкет и два вида участников."""


class AnketaError(Exception):
    """Ошибка заполнения анкеты."""


class Person:
    def __init__(self, fio, email, phone):
        self.fio = self.fix_fio(fio)
        self.email = self.fix_email(email)
        self.phone = self.fix_phone(phone)

    @staticmethod
    def fix_fio(raw):
        pieces = raw.split()
        if len(pieces) < 2:
            raise AnketaError("ФИО состоит меньше чем из двух слов")
        return " ".join(part.capitalize() for part in pieces)

    @staticmethod
    def fix_email(raw):
        value = raw.strip().lower()
        if value.count("@") != 1 or any(ch.isspace() for ch in value):
            raise AnketaError("ошибка в записи почты")
        login, host = value.split("@")
        if not login or not host or "." not in host:
            raise AnketaError("адрес почты неполный")
        if host.startswith(".") or host.endswith("."):
            raise AnketaError("домен почты неверный")
        return value

    @staticmethod
    def fix_phone(raw):
        numbers = "".join(ch for ch in raw if ch.isdigit())
        if len(numbers) != 11:
            raise AnketaError(f"в телефоне {len(numbers)} цифр вместо 11")
        if numbers[0] not in ("7", "8"):
            raise AnketaError("телефон начинается не с 7 и не с 8")
        return "7" + numbers[1:]

    def masked_phone(self):
        return f"+7 ({self.phone[1:4]}) ***-**-{self.phone[-2:]}"

    def short_fio(self):
        chunks = self.fio.split()
        return chunks[0] + " " + " ".join(piece[0] + "." for piece in chunks[1:])

    def role(self):
        return "участник"

    def extra(self):
        return "—"

    def group_key(self):
        return None

    def __str__(self):
        return f"{self.fio} | {self.role()} | {self.extra()}"

    def __lt__(self, other):
        return self.fio < other.fio


class Student(Person):
    def __init__(self, fio, email, phone, group):
        super().__init__(fio, email, phone)
        self.group = "".join(group.split()).lower()
        if not self.group:
            raise AnketaError("пустая группа")

    def role(self):
        return "студент"

    def extra(self):
        return self.group

    def group_key(self):
        return self.group


class Teacher(Person):
    def __init__(self, fio, email, phone, department):
        super().__init__(fio, email, phone)
        self.department = " ".join(department.split())
        if not self.department:
            raise AnketaError("кафедра не указана")

    def role(self):
        return "преподаватель"

    def extra(self):
        return self.department


if __name__ == "__main__":
    item = Student("Федорова Марина", "marina@post.ru", "89112223344", "09с41")
    print(item, item.masked_phone())
