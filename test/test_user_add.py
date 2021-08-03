from model.user import User


def test_add_user_wo_group(app):
    app.session.login(user_name=app.user_name, user_pass=app.user_pass)
    app.user.add_new_wo_group(User(first_name=app.first_name, middle_name=app.middle_name, last_name=app.last_name))
    app.session.logout()
