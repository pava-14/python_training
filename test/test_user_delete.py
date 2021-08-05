__author__ = 'apavlenko'

from model.user import User


def test_user_delete_first(app):
    if app.user.count() == 0:
        app.user.add_new_wo_group(User(first_name=app.first_name, middle_name=app.middle_name, last_name=app.last_name))
    app.user.delete_first()


def test_user_delete_by_full_name(app):
    first_name = "Bob_8GQOOY"
    last_name = "Marley_8GQOOY"
    app.user.delete_by_name(first_name, last_name)
