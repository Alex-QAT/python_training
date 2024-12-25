from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        self.start_create()
        self.fill_gr(group)
        self.complete_create()
        # кэш теряет актуалность
        self.group_cache = None

    def edit_1st(self, group):
        self.edit_by_index(0, group)

    def edit_by_index(self, index, group):
        self.start_edit_by_index(index)
        self.fill_gr(group)
        self.complete_edit()
        # кэш теряет актуалность
        self.group_cache = None

    def start_edit_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        # init group edition
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_name("edit").click()

    def edit_by_id(self, id, group):
        self.start_edit_by_id(id)
        self.fill_gr(group)
        self.complete_edit()
        # кэш теряет актуалность
        self.group_cache = None

    def start_edit_by_id(self, id):
        wd = self.app.wd
        self.open_group_page()
        # init group edition
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        wd.find_element_by_name("edit").click()

    def del_1st_gr(self):
        self.del_gr_by_index(0)

    def del_gr_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        #select group by index
        wd.find_elements_by_name("selected[]")[index].click()
        #submit delete group
        wd.find_element_by_name("delete").click()
        # return to group page
        self.return_to_group_page()
        # кэш теряет актуалность
        self.group_cache = None

    def del_gr_by_id(self, id):
        wd = self.app.wd
        self.open_group_page()
        # select group by id
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        # submit delete group
        wd.find_element_by_name("delete").click()
        # return to group page
        self.return_to_group_page()
        # кэш теряет актуалность
        self.group_cache = None




    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def fill_gr(self, group):
        wd = self.app.wd
        # fill group form
        self.chng_fld_gr("group_name", group.name)
        self.chng_fld_gr("group_header", group.header)
        self.chng_fld_gr("group_footer", group.footer)

    def chng_fld_gr(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

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




    #def start_edit_1st(self):
    #    wd = self.app.wd
    #    self.open_group_page()
    #    # init group edition
    #    wd.find_element_by_name("selected[]").click()
    #    wd.find_element_by_name("edit").click()

    def complete_edit(self):
        wd = self.app.wd
        # submit group edition
        wd.find_element_by_name("update").click()
        self.return_to_group_page()



    def count_gr(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None
    # метод получения списка групп
    def get_gr_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

