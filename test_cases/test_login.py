import pytest
from selenium import webdriver
from page_objects.LoginPage import LoginPage
from test_cases.configTest import *
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGenerator


class TestLogin:
    log = LogGenerator.log_gen()

    @pytest.mark.sanity
    def test_homepage_title(self, setup):
        self.driver = setup
        self.driver.get(Readconfig.get_app_url())
        self.log.info("Navigated to URL:" + Readconfig.get_app_url())
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()
        self.log.info("*****test_homepage_title Started*****")
        actual_title = self.driver.title
        if actual_title == "Your Store":
            assert True
            self.driver.quit()
            self.log.info("test_homepage_title passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage_title.png")
            self.driver.quit()
            self.log.info("test_homepage_title failed")
            assert False
        # assert actual_title == "Your Store", "Title is not matched"
        self.log.info("*****test_homepage_title Completed*****")

    @pytest.mark.smoke
    def test_login_successful(self, setup):
        self.driver = setup
        self.driver.get(Readconfig.get_app_url())
        self.log.info("Navigated to URL:" + Readconfig.get_app_url())
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.log.info("*****test_login_successful Started*****")
        self.login_page = LoginPage(self.driver)
        self.login_page.click_login_header()
        self.login_page.enter_login_credentials(Readconfig.get_username(), Readconfig.get_password())
        self.login_page.click_submit_login()
        actual_title = self.driver.title
        if actual_title == "My Account":
            assert True
            self.driver.quit()
            self.log.info("test_login_successful passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage_title.png")
            self.driver.quit()
            self.log.info("test_login_successful failed")
            assert False
        self.log.info("*****test_login_successful Completed*****")
