
class GroupHelper:

    def create(self,group):
        self.start_create()
        self.fill_gr(group)
        self.complete_create()

    def edit_1st(self,group):
        self.start_edit_1st()
        self.fill_gr(group)
        self.complete_edit()

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def fill_gr(self, group):
        wd = self.app.wd
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)


    def start_create(self):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()

    def complete_create(self):
        wd = self.app.wd
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()


    def start_edit_1st(self):
        wd = self.app.wd
        self.open_group_page()
        # init group edition
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()

    def complete_edit(self):
        wd = self.app.wd
        # submit group edition
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def del_1st_gr(self):
        wd = self.app.wd
        self.open_group_page()
        #select group
        wd.find_element_by_name("selected[]").click()
        #submit delete group
        wd.find_element_by_name("delete").click()
        # return to group page
        self.return_to_group_page()