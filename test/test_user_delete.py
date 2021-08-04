__author__ = 'apavlenko'


def test_user_delete(app):
    first_name = "Bob_8GQOOY"
    last_name = "Marley_8GQOOY"
    app.session.login(user_name=app.user_name, user_pass=app.user_pass)
    app.user.delete_by_name(first_name, last_name)
    app.session.logout()
