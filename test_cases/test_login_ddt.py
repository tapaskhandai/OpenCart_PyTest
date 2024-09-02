import allure
from allure_commons.types import AttachmentType

from page_objects_controls.LoginPageControls import LoginPageControls
from page_objects_controls.MyAccountPageControls import MyAccountPageControls
from test_cases.configTest import *
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGenerator
from utilities.XLUtils import *
from utilities.seleniumUtilities import SeleniumUtilities


class TestLoginDDT:
    log = LogGenerator.log_gen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.driver = setup
        self.log.info("*****test_login_ddt Started*****")

        self.login_page = LoginPageControls(self.driver)
        self.login_page.get_link_my_account().click()
        self.login_page.get_link_login_my_account().click()
        self.rows = get_row_count(Readconfig.get_excel_file_path(), "Sheet1")
        for r in range(2, self.rows + 1):
            username = read_data(Readconfig.get_excel_file_path(), "Sheet1", r, 1)
            password = read_data(Readconfig.get_excel_file_path(), "Sheet1", r, 2)
            exp_status = read_data(Readconfig.get_excel_file_path(), "Sheet1", r, 3)
            SeleniumUtilities.enter_text(self, self.login_page.get_textbox_email_login(), username)
            SeleniumUtilities.enter_text(self, self.login_page.get_textbox_password_login(), password)
            self.login_page.get_button_submit_login().click()
            actual_title = self.driver.title
            if actual_title == "My Account" and exp_status == "Pass":
                assert True
                self.log.info("Login Successful")
                self.log.info("test_login_ddt Passed")
                self.login_page.get_link_my_account().click()
                self.my_account_page = MyAccountPageControls(self.driver)
                self.my_account_page.get_button_logout_homepage().click()
                self.my_account_page.get_button_continue_homepage().click()
                self.login_page.get_link_my_account().click()
                self.login_page.get_link_login_my_account().click()
            elif actual_title != "My Account" and exp_status == "Fail":
                assert True
                self.log.info("Login Unsuccessful")
                self.log.info("test_login_ddt Passed")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "est_login_ddt.png")
                allure.attach(self.driver.get_screenshot_as_png(), name="title", attachment_type=AttachmentType.PNG)
                self.log.info("test_login_ddt Failed")
                assert False
            self.log.info("*****test_login_ddt Completed*****")
