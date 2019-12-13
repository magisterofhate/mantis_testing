from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Helpers:

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

    def wait_for_element(self, path, timeout=10):
        wd = self.wd
        wait = WebDriverWait(wd, timeout)
        wait.until(ec.visibility_of_element_located((By.XPATH, path)))