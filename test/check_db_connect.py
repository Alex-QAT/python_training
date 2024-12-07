from fixture.orm import ORMFixture
from model.group import Group

#db = ORMFixture(host="127.0.0.1", db_name="addressbook", user="root", password="b0r0v@Y@")
def test_check(orm):
    try:
        l = orm.get_con_not_in_gr(Group(id="454"))
        for item in l:
            print('')
            print(item)
        print(len(l))
    finally:
        pass

