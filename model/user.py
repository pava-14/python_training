# ~*~ coding: utf-8 ~*~
from sys import maxsize


class User:

    def __init__(self, first_name=None, middle_name=None, last_name=None, id=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.first_name, self.middle_name, self.last_name,)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.first_name == other.first_name and self.last_name == other.last_name
        # and (self.middle_name == other.middle_name or \
        #      self.middle_name is None or other.middle_name is None) \

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
