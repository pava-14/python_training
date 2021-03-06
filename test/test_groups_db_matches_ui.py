__author__ = 'apavlenko'

from timeit import timeit

from model.group import Group


def test_group_list(app, db):
    ui_list = app.group.get_group_list()

    def clean(group):
        return Group(id=group.id, name=group.name.strip())

    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_group_list_time(app, db):
    print("\nUI:", timeit(lambda: app.group.get_group_list(), number=1))

    def clean(group):
        return Group(id=group.id, name=group.name.strip())

    print("DB:", timeit(lambda: map(clean, db.get_group_list()), number=1000))
    assert False  # assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
