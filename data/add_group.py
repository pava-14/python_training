__author__ = 'apavlenko'

from model.group import Group
from util.datagenerator import random_string

constant = [
    Group(name="group1", header="header1", footer="footer1"),
    Group(name="group2", header="header2", footer="footer2"),
    Group(name="group2", header="header2", footer="footer2"),
]

testdata = [
    Group(name=random_string("name_", 10), header=random_string("header_", 20), footer=random_string("footer_", 20))
    for i in range(1)
]

# testdata = [Group(name="", header="", footer="")] + [
#     Group(name=random_string("name_", 10), header=random_string("header_", 20), footer=random_string("footer_", 20))
#     for i in range(5)
# ]
