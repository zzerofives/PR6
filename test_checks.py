from pathlib import Path
import pytest
from people import AnketaError, Person, Student, Teacher
from registry import Registry, parse_line


def test_student():
    p = Student("   фЕДОРОВА    МАРИНА ", " MARINA@POST.RU ", "8 911 222 33 44", " 09С41 ")
    assert p.fio == "Федорова Марина"
    assert p.extra() == "09с41"
    assert p.short_fio() == "Федорова М."


def test_teacher():
    p = Teacher("Романов Илья", "romanov@site.ru", "89112223344", "Кафедра ИТ")
    assert p.role() == "преподаватель"


def test_invalid():
    with pytest.raises(AnketaError):
        Student("Илья", "a@b.ru", "89112223344", "09с41")


def test_type():
    with pytest.raises(AnketaError):
        parse_line("x;Иван Иванов;aa@bb.ru;89112223344;09с41")


def test_registry():
    reg = Registry()
    assert reg.load(Path(__file__).with_name("anketa.txt"))
    assert len(reg) >= 5
    assert len(reg.errors) >= 4
    assert reg.role_stats()["студент"] >= 1


def test_missing():
    reg = Registry()
    assert reg.load("__not_existing_file__.txt") is False
