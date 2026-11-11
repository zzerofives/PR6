"""Запуск объектно-ориентированного обработчика анкет."""
from pathlib import Path
import sys
from registry import Registry

def show_results(journal):
    persons = sorted(journal.people)
    fio_width = max([22] + [len(person.fio) for person in persons])
    extra_width = max([16] + [len(person.extra()) for person in persons])
    print(f"{'№':>3}  {'ФИО':<{fio_width}}  {'Роль':<14}  "
          f"{'Группа/кафедра':<{extra_width}}  Телефон")
    print("-" * 92)
    for index, person in enumerate(persons, start=1):
        print(f"{index:>3}  {person.fio:<{fio_width}}  {person.role():<14}  "
              f"{person.extra():<{extra_width}}  {person.masked_phone()}")
    print("-" * 92)
    print(f"Принято: {len(journal)}. Отклонено: {len(journal.errors)}.")
    for number, reason, raw in journal.errors:
        print(f"  Ошибка в строке {number}: {reason}\n    {raw}")
    print("По ролям:")
    for role, amount in sorted(journal.role_stats().items()):
        print(f"  {role}: {amount}")
    print("По группам:")
    for group, amount in sorted(journal.group_stats().items()):
        print(f"  {group}: {amount}")

def main():
    source = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("anketa.txt")
    journal = Registry()
    try:
        found = journal.load(source)
    except (UnicodeError, OSError) as error:
        print("Ошибка при чтении:", error)
        return
    if not found:
        print(f"Файл {source.name} не найден")
        return
    show_results(journal)
    try:
        journal.save_ok(source.with_name("ok.txt"))
        journal.save_errors(source.with_name("errors.txt"))
    except OSError as error:
        print("Не удалось сохранить результат:", error)
        return
    print("Файлы ok.txt и errors.txt сохранены")

if __name__ == "__main__":
    main()
