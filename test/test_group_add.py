__author__ = 'apavlenko'

from model.group import Group


def test_group_add(app):
    app.group.create(Group(name=app.group_name, header=app.group_header,
                           footer=app.group_footer))

# def test_empty_group_add(app):
#     app.group.create(Group(name="", header="", footer=""))
