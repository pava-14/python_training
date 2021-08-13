__author__ = 'apavlenko'

import random
import string

from faker import Faker


def get_random_string(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def get_randomx_string():
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(random.randrange(20))])


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_with_space(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_with_space_punct(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_firstname():
    fake = Faker()
    return fake.first_name()


def random_lastname():
    fake = Faker()
    return fake.last_name()


def random_email():
    fake = Faker()
    return fake.email()


def random_phonenumber():
    fake = Faker()
    return fake.phone_number()


def random_stret_address():
    fake = Faker()
    return fake.street_address()


def random_short_middlename():
    return get_random_string(size=1, chars=string.ascii_uppercase)
