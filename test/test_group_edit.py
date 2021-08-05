__author__ = 'apavlenko'


def test_group_edit_by_name(app):
    app.session.login(user_name=app.user_name, user_pass=app.user_pass)
    app.group.edit_by_name("Group_I0KPNM")
    app.session.logout()
