from fixture.helpers import Helpers as helpers


class Navigation:

    def __init__(self, app):
        self.app = app
        self.helpers = helpers(self.app)

    def home_page(self):
        wd = self.app.wd
        if not ((wd.current_url.endswith("/mantisbt-2.22.1/") or wd.current_url.endswith("/my_view_page.php")) and len(
                wd.find_elements_by_xpath("//a[@title='Написать веб-мастеру по эл. почте']")) > 0):
            wd.get(self.app.base_url)
        self.helpers.wait_for_element("//body")

    def projects_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//i[@class='menu-icon fa fa-gears']").click()
        wd.find_element_by_link_text('Управление проектами').click()

    def login(self, user='administrator', pwd='root'):
        self.home_page()
        self.app.wd.find_element_by_xpath("//input[@id='username']").send_keys(user)
        self.app.wd.find_element_by_xpath("//input[@type='submit']").click()
        self.helpers.wait_for_element("//input[@type='password']")
        self.app.wd.find_element_by_name("password").send_keys(pwd)
        self.app.wd.find_element_by_xpath("//input[@type='submit']").click()

    def logout(self):
        self.app.wd.get("http://10.201.48.35/mantisbt-2.22.1/logout_page.php")
        self.helpers.wait_for_element("//input[@name='username']")

    def int_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        return len(self.app.wd.find_elements_by_xpath("//a/span[@class = 'smaller-75']")) > 0

    def int_login(self, user, pwd):
        if self.is_logged_in():
            if self.is_logged_in_as(user):
                return
            else:
                self.logout()
        self.login(user, pwd)

    def is_logged_in_as(self, user):
        return self.app.wd.find_elements_by_xpath("//a/span[@class = 'user-info']") == user


