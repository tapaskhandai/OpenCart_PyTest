import time

from page_objects_controls.LoginPageControls import LoginPageControls
from test_cases.config_test import *
from utilities.customLogger import LogGenerator
from utilities.readProperties import Readconfig
from utilities.seleniumUtilities import SeleniumUtilities
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.usefixtures("setup")  # Automatically use the setup fixture
class TestLogin:
    driver: WebDriver  # 👈 Tell the IDE this attribute exists
    log = LogGenerator.log_gen()

    @pytest.mark.sanity
    def test_application_title(self):
        self.log.info("***** test_application_title Started *****")
        actual_title = self.driver.title
        assert actual_title == "Your Store1"
        self.log.info("test_application_title passed")
        self.log.info("***** test_application_title Completed *****")

    @pytest.mark.smoke1
    def test_login_scenarios(self):
        self.log.info("*****test_login_scenarios started*****")
        self.login_page = LoginPageControls(self.driver)
        self.login_page.get_link_my_account().click()
        self.login_page.get_link_login_my_account().click()
        SeleniumUtilities.enter_text(self, self.login_page.get_textbox_email_login(), Readconfig.get_username())
        SeleniumUtilities.enter_text(self, self.login_page.get_textbox_password_login(), Readconfig.get_password())
        self.login_page.get_button_submit_login().click()
        actual_title = self.driver.title
        time.sleep(1)
        assert actual_title == "My Account"
        self.log.info("test_login_scenarios passed")
        self.log.info("*****test_login_scenarios Completed*****")
