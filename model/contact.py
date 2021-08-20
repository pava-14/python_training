# ~*~ coding: utf-8 ~*~
from sys import maxsize


class Contact:

    def __init__(self, id=None,
                 firstname=None, middlename=None, lastname=None, fullname=None, address=None,
                 home_phone=None, mobile_phone=None, work_phone=None, secondary_phone=None, all_phones=None,
                 f_email=None, s_email=None, t_email=None, all_emails=None):
        self.id = id
        # name
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.fullname = fullname
        # address
        self.address = address
        # phone
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone
        self.all_phones = all_phones
        # email
        self.f_email = f_email
        self.s_email = s_email
        self.t_email = t_email
        self.all_emails = all_emails

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.firstname, self.middlename, self.lastname,)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.firstname == other.firstname and self.lastname == other.lastname
        # and (self.middle_name == other.middle_name or \
        #      self.middle_name is None or other.middle_name is None) \

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
