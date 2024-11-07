from selenium.webdriver.support.select import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add_new(self,contact):
        self.start_add()
        self.fill_contact(contact)
        self.complete_add()

    def edit_1st(self,contact):
        self.start_edit_1st()
        self.fill_contact(contact)
        self.complete_edit()

    def start_add(self):
        wd = self.app.wd
        self.open_homepage()
        # init new contact creation
        wd.find_element_by_link_text("add new").click()

    def open_homepage(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.get("http://localhost/addressbook/")

    def complete_add(self):
        wd = self.app.wd
        # form input
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        # return_to_homepage
        self.return_to_homepage()

    def start_edit_1st(self):
        wd = self.app.wd
        self.open_homepage()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def complete_edit(self):
        wd = self.app.wd
        # update submit
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        # return_to_homepage
        self.return_to_homepage()


    def del_1st_con(self):
        wd = self.app.wd
        self.open_homepage()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()


    def chng_fld_con(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)



    def fill_contact(self, contact):
        wd = self.app.wd
        # fill contact form
        self.chng_fld_con("firstname", contact.firstname)
        #wd.find_element_by_name("firstname").click()
        #wd.find_element_by_name("firstname").clear()
        #wd.find_element_by_name("firstname").send_keys(contact.firstname)
        self.chng_fld_con("middlename", contact.midlename)
        #wd.find_element_by_name("middlename").click()
        #wd.find_element_by_name("middlename").clear()
        #wd.find_element_by_name("middlename").send_keys(contact.midlename)
        self.chng_fld_con("lastname", contact.lastname)
        #wd.find_element_by_name("lastname").click()
        #wd.find_element_by_name("lastname").clear()
        #wd.find_element_by_name("lastname").send_keys(contact.lastname)
        #wd.find_element_by_name("theform").click()
        self.chng_fld_con("nickname", contact.nickname)
        #wd.find_element_by_name("nickname").click()
        #wd.find_element_by_name("nickname").clear()
        #wd.find_element_by_name("nickname").send_keys(contact.nickname)
        #wd.find_element_by_name("theform").click()
        # add foto-file
        # driver.find_element_by_name("photo").click()
        # driver.find_element_by_name("photo").clear()
        # driver.find_element_by_name("photo").send_keys(u"D:\1.jpg")
        self.chng_fld_con("title", contact.tittle)
        #wd.find_element_by_name("title").click()
        #wd.find_element_by_name("title").clear()
        #wd.find_element_by_name("title").send_keys(contact.tittle)
        self.chng_fld_con("company", contact.company)
        #wd.find_element_by_name("company").click()
        #wd.find_element_by_name("company").clear()
        #wd.find_element_by_name("company").send_keys(contact.company)
        self.chng_fld_con("address", contact.address)
        #wd.find_element_by_name("address").click()
        #wd.find_element_by_name("address").clear()
        #wd.find_element_by_name("address").send_keys(contact.address)
        self.chng_fld_con("home", contact.home)
        #wd.find_element_by_name("home").click()
        #wd.find_element_by_name("home").clear()
        #wd.find_element_by_name("home").send_keys(contact.home)
        self.chng_fld_con("mobile", contact.mobile)
        #wd.find_element_by_name("mobile").click()
        #wd.find_element_by_name("mobile").clear()
        #wd.find_element_by_name("mobile").send_keys(contact.mobile)
        self.chng_fld_con("work", contact.work)
        #wd.find_element_by_name("work").click()
        #wd.find_element_by_name("work").clear()
        #wd.find_element_by_name("work").send_keys(contact.work)
        #wd.find_element_by_name("theform").click()
        self.chng_fld_con("fax", contact.fax)
        #wd.find_element_by_name("fax").click()
        #wd.find_element_by_name("fax").clear()
        #wd.find_element_by_name("fax").send_keys(contact.fax)
        #wd.find_element_by_name("theform").click()
        self.chng_fld_con("email", contact.email)
        #wd.find_element_by_name("email").click()
        #wd.find_element_by_name("email").clear()
        #wd.find_element_by_name("email").send_keys(contact.email)
        self.chng_fld_con("email2", contact.email2)
        #wd.find_element_by_name("email2").click()
        #wd.find_element_by_name("email2").clear()
        #wd.find_element_by_name("email2").send_keys(contact.email2)
        self.chng_fld_con("email3", contact.email3)
        #wd.find_element_by_name("email3").click()
        #wd.find_element_by_name("email3").clear()
        #wd.find_element_by_name("email3").send_keys(contact.email3)
        self.chng_fld_con("homepage", contact.homepage)
        #wd.find_element_by_name("homepage").click()
        #wd.find_element_by_name("homepage").clear()
        #wd.find_element_by_name("homepage").send_keys(contact.homepage)

        #wd.find_element_by_name("bday").click()
        self.chng_slct_fld("bday", contact.bday)
        #wd.find_element_by_xpath("//option[@value=%s]" % contact.bday).click()
        #wd.find_element_by_name("bmonth").click()
        self.chng_slct_fld("bmonth", contact.bmonth)
        #Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        #wd.find_element_by_xpath("//option[@value=%s]" % contact.bmonth_x).click()
        self.chng_fld_con("byear", contact.byear)
        #wd.find_element_by_name("byear").click()
        #wd.find_element_by_name("byear").clear()
        #wd.find_element_by_name("byear").send_keys(contact.byear)
        #wd.find_element_by_name("aday").click()
        self.chng_slct_fld("aday", contact.aday)
        #Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        #wd.find_element_by_xpath("//div[@id='content']/form/select[3]/option[%s]" % contact.aday_x).click()
        #wd.find_element_by_name("amonth").click()
        self.chng_slct_fld("amonth", contact.amonth)
        #Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        #wd.find_element_by_xpath("//div[@id='content']/form/select[4]/option[%s]" % contact.amonth_x).click()
        self.chng_fld_con("ayear", contact.ayear)
        #wd.find_element_by_name("ayear").click()
        #wd.find_element_by_name("ayear").clear()
        #wd.find_element_by_name("ayear").send_keys(contact.ayear)
        #wd.find_element_by_name("theform").click()

    def chng_slct_fld(self, fld_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(fld_name)).select_by_visible_text(text)

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count_con(self):
        wd = self.app.wd
        self.open_homepage()
        return len(wd.find_elements_by_name("selected[]"))
