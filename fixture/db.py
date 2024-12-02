import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, db_name, user, password):
        self.host = host
        self.db_name = db_name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=db_name, user=user, password=password, autocommit=True)

    #получение списка групп из БД
    def get_gr_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_con_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, title, company, address, home, mobile, work, fax, email, email2, email3, homepage, bday, bmonth, byear, aday, amonth, ayear from addressbook")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, title, company, address, home, mobile, work, fax, email, email2, email3, homepage, bday, bmonth, byear, aday, amonth, ayear) = row
                list.append(Contact(id=str(id), firstname=firstname, midlename=middlename, lastname=lastname, nickname=nickname, tittle=title, company=company, address=address, home=home, mobile=mobile, work=work, fax=fax, email=email, email2=email2, email3=email3, homepage=homepage, bday=bday, bmonth=bmonth, byear=byear, aday=aday, amonth=amonth, ayear=ayear))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()