from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", db_name="addressbook", user="root", password="b0r0v@Y@")

try:
    l = db.get_con_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass

