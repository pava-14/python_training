__author__ = 'apavlenko'

import random
import string


def get_random_string(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def get_randomx_string():
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(random.randrange(20))])
