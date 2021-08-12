__author__ = 'apavlenko'

import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.user.get_user_list_from_home_page()[0]
    contact_from_edit_page = app.user.get_user_info_from_edit_page(0)
    assert contact_from_home_page.all_phones == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_home_page = app.user.get_user_list_from_home_page()[0]
    contact_from_view_page = app.user.get_user_info_from_view_page(0)
    assert contact_from_home_page.all_phones == contact_from_view_page.all_phones


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                              [user.home_phone, user.work_phone, user.mobile_phone,
                                               user.secondary_phone]))))
