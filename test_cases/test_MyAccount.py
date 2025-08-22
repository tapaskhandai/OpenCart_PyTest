from allure_commons.types import AttachmentType
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects_controls.LoginPageControls import LoginPageControls
from page_objects_controls.MyAccountPageControls import MyAccountPageControls
from test_cases.conftest import *
from utilities.customLogger import LogGenerator
from utilities.readProperties import Readconfig
from utilities.seleniumUtilities import *


@pytest.mark.usefixtures("setup")  # Automatically use the setup fixture
class TestMyAccount:
    driver: WebDriver
    log = LogGenerator.log_gen()

    @pytest.mark.sanity1
    def test_edit_your_account_info(self):
        self.log.info("***** test_edit_your_account_info Started *****")

        self.login_page = LoginPageControls(self.driver)
        self.login_page.get_link_my_account().click()
        self.login_page.get_link_login_my_account().click()
        SeleniumUtilities.enter_text(self.login_page.get_textbox_email_login(), Readconfig.get_username())
        SeleniumUtilities.enter_text(self.login_page.get_textbox_password_login(), Readconfig.get_password())
        self.login_page.get_button_submit_login().click()
        self.log.info("test login successful")
        a = 5 / 0
        self.my_account_page = MyAccountPageControls(self.driver)
        self.my_account_page.get_link_edit_account_info().click()
        SeleniumUtilities.enter_text(self.my_account_page.get_textbox_firstname_edit_info(), "Firstname")
        SeleniumUtilities.enter_text(self.my_account_page.get_textbox_lastname_edit_info(), "LastName")
        SeleniumUtilities.enter_text(self.my_account_page.get_textbox_telnum_edit_info(), "6785432")
        self.my_account_page.get_button_continue_edit_info().click()
        account_update_msg = SeleniumUtilities.get_text(self.my_account_page.get_success_msg_account_updated())
        assert account_update_msg == "Success: Your account has been successfully updated."

        SeleniumUtilities.mouse_hover_on_element(self.driver, self.my_account_page.get_link_components())
        self.log.info("test_edit_your_account_info is Passed")
        self.log.info("*****test_edit_your_acc_info Completed*****")

    @pytest.mark.smoke
    def test_change_password_negative(self):
        self.log.info("*****test_change_password_negative*****")

        self.login_page = LoginPageControls(self.driver)
        self.login_page.get_link_my_account().click()
        self.login_page.get_link_login_my_account().click()
        SeleniumUtilities.enter_text(self.login_page.get_textbox_email_login(), Readconfig.get_username())
        SeleniumUtilities.enter_text(self.login_page.get_textbox_password_login(), Readconfig.get_password())
        self.login_page.get_button_submit_login().click()
        self.log.info("test login successful")

        self.my_account_page = MyAccountPageControls(self.driver)
        self.my_account_page.get_link_change_password().click()
        SeleniumUtilities.enter_text(self.my_account_page.get_textbox_password_change_password(), "abcde")
        SeleniumUtilities.enter_text(self.my_account_page.get_textbox_confirm_password_change_password(), "987654")

        self.my_account_page.get_button_continue_edit_info().click()
        assert SeleniumUtilities.element_is_displayed(self.my_account_page.get_error_msg_change_password())
        self.log.info("test_change_password_negative is Passed")

        self.log.info("*****test_change_password_negative Completed*****")
