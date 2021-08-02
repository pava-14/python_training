import pytest

from model.user import User
from fixture.userbase import UserPageBase


@pytest.fixture
def user_page(request):
    fixture = UserPageBase()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_user(user_page):
    user_page.login(user_name=user_page.user_name, user_pass=user_page.user_pass)
    user_page.add_new_user_wo_group(
        User(first_name=user_page.first_name, middle_name=user_page.middle_name, last_name=user_page.last_name))
    user_page.logout()
