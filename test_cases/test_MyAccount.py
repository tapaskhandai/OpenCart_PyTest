from page_objects.LoginPage import LoginPage
from page_objects.MyAccountPage import MyAccountPage
from test_cases.configTest import *
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGenerator


class TestMyAccount:
    log = LogGenerator.log_gen()

    @pytest.mark.sanity
    def test_edit_your_acc_info(self, setup):
        self.driver = setup
        self.log.info("*****test_edit_your_acc_info Started*****")

        self.login_page = LoginPage(self.driver)
        self.login_page.click_login_header()
        self.login_page.enter_login_credentials(Readconfig.get_username(), Readconfig.get_password())
        self.login_page.click_submit_login()
        self.log.info("test login successful")

        self.my_account_page = MyAccountPage(self.driver)
        self.my_account_page.click_edit_your_account_info()
        self.my_account_page.enter_personal_details("Firstname", "LastName", "9874908")
        self.my_account_page.click_continue_my_account()
        account_update_msg = self.my_account_page.capture_success_msg_account_updated()
        if account_update_msg == "Success: Your account has been successfully updated.":
            assert True
            self.log.info("test_edit_your_acc_info is Passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_edit_your_acc_info.png")
            self.log.info("test_edit_your_acc_info is Failed")
            assert False
        self.driver.quit()
        self.log.info("*****test_edit_your_acc_info Completed*****")

    @pytest.mark.smoke
    def test_change_password_negative(self, setup):
        self.driver = setup
        self.log.info("*****test_change_password_negative*****")

        self.login_page = LoginPage(self.driver)
        self.login_page.click_login_header()
        self.login_page.enter_login_credentials(Readconfig.get_username(), Readconfig.get_password())
        self.login_page.click_submit_login()
        self.log.info("test login successful")

        self.my_account_page = MyAccountPage(self.driver)
        self.my_account_page.click_change_your_password()
        self.my_account_page.enter_password_and_confirm_password("abcde", "12345")
        self.my_account_page.click_continue_my_account()
        try:
            if self.my_account_page.capture_error_msg_change_password():
                assert True
                self.log.info("test_change_password_negative is Passed")
        except:
            self.log.info("Exception Occurs")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_change_password_negative.png")
            self.log.info("test_change_password_negative is Failed")
            assert False

        self.driver.quit()
        self.log.info("*****test_change_password_negative Completed*****")
