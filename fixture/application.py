# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from fixture.navigation import Navigation
import warnings


class Application:

    def __init__(self, browser, base_url):
        if browser == "ff":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            warnings.warn("Unrecognized browser %s. Used default" % browser, Warning)
            self.wd = webdriver.Firefox()
        self.select = webdriver.support.ui.Select
        self.wd.implicitly_wait(2)
        self.navigation = Navigation(self)
        self.base_url = base_url

    def destroy(self):
        self.wd.quit()

    def is_session_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

