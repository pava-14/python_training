# ~*~ coding: utf-8 ~*~
import string
import random


def get_random_string(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class Group:

    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer
