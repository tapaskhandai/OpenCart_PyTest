import allure
from allure_commons.types import AttachmentType
from page_objects_controls.LoginPageControls import LoginPageControls
from test_cases.configTest import *
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGenerator
from utilities.seleniumUtilities import SeleniumUtilities


class TestLogin:
    log = LogGenerator.log_gen()

    @pytest.mark.sanity
    def test_application_title(self, setup):
        self.driver = setup
        self.log.info("*****test_application_title Started*****")
        actual_title = self.driver.title
        if actual_title == "Your Store":
            assert True
            self.driver.quit()
            self.log.info("test_application_title passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage_title.png")
            self.driver.quit()
            self.log.info("test_application_title failed")
            assert False
        # assert actual_title == "Your Store", "Title is not matched"
        self.log.info("*****test_application_title Completed*****")

    @pytest.mark.smoke1
    def test_login_scenarios(self, setup):
        self.driver = setup
        self.log.info("*****test_login_scenarios started*****")
        self.login_page = LoginPageControls(self.driver)
        self.login_page.get_link_my_account().click()
        self.login_page.get_link_login_my_account().click()
        SeleniumUtilities.enter_text(self, self.login_page.get_textbox_email_login(), Readconfig.get_username())
        SeleniumUtilities.enter_text(self, self.login_page.get_textbox_password_login(), Readconfig.get_password())
        self.login_page.get_button_submit_login().click()
        actual_title = self.driver.title
        if actual_title == "My Account":
            assert True
            self.driver.quit()
            self.log.info("test_login_scenarios passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_scenarios.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="title", attachment_type=AttachmentType.PNG)
            self.driver.quit()
            self.log.info("test_login_scenarios failed")
            assert False
        self.log.info("*****test_login_scenarios Completed*****")
