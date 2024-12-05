from pony.orm import *

from model.group import Group
from model.contact import Contact

class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        home = Optional(str, column='home')
        mobile = Optional(str, column='mobile')
        work = Optional(str, column='work')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        address = Optional(str, column='address')

    def __init__(self, host, db_name, user, password):
        self.db.bind('mysql', host=host, database=db_name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)


    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))


    @db_session
    def get_gr_list(self):
        return self.convert_groups_to_model(list(select(g for g in ORMFixture.ORMGroup)))

    def convert_con_to_model(self, cons):
        def convert(con):
            return Contact(id=str(con.id), firstname=con.firstname, lastname=con.lastname, home=con.home, mobile=con.mobile, work=con.work, email=con.email, email2=con.email2, email3=con.email3, address=con.address)

        return list(map(convert, cons))

    @db_session
    def get_con_list(self):
        return self.convert_con_to_model(list(select(c for c in ORMFixture.ORMContact)))

