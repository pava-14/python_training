__author__ = 'apavlenko'

import getopt
import os.path
import sys

import jsonpickle

from model.user import User
from util.datagenerator import *

try:
    opts, args = getopt.getopt(sys.argv[1:], "nu:fu:", ["number of users", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

# default parameters
nu = 5
out = "data/users.json"

for o, a in opts:
    if o == "-nu":
        nu = int(a)
    elif o == "-fu":
        out = a

# testdata = [User(first_name="", middle_name="", last_name="")] + \
testdata = [User(firstname=random_firstname(), middlename=random_short_middlename(), lastname=random_lastname(),
                 address=random_stret_address(),
                 f_email=random_email(), s_email=random_email(), t_email=random_email(),
                 home_phone=random_phonenumber(), mobile_phone=random_phonenumber(), work_phone=random_phonenumber())
    for i in range(nu)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", out)
with open(file, "w") as f:
    jsonpickle.set_encoder_options("json", indent=2)
    f.write(jsonpickle.encode(testdata))
