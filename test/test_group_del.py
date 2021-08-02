

def test_group_add(app):
    app.session.login(user_name=app.user_name, user_pass=app.user_pass)
    app.group.delete_first_group()
    # TODO: Check for group_name
    # do something
    app.session.logout()
