__author__ = 'apavlenko'

# import json
import jsonpickle
import getopt
import sys

from model.group import Group
from util.datagenerator import random_string
import os.path

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of group", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
out = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        out = a

testdata = [
    Group(name=random_string("name_", 10), header=random_string("header_", 20), footer=random_string("footer_", 20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", out)
# with open(file, "w") as f:
#     f.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
with open(file, "w") as f:
    jsonpickle.set_encoder_options("json", indent=2)
    f.write(jsonpickle.encode(testdata))
