__author__ = 'apavlenko'


def test_group_delete_first_group(app):
    app.session.login(user_name=app.user_name, user_pass=app.user_pass)
    app.group.delete_first()
    app.session.logout()


def test_group_delete_by_name(app):
    app.session.login(user_name=app.user_name, user_pass=app.user_pass)
    app.group.delete_by_name("Group_8E9JTK_edited")
    app.session.logout()
