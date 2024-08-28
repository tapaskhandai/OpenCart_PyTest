from page_objects.LoginPage import LoginPage
from test_cases.configTest import *
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGenerator
from utilities.XLUtils import *


class TestLoginDDT:
    log = LogGenerator.log_gen()
    path = ".//TestData/data_driven_PyTest.xlsx"

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.driver = setup
        self.driver.get(Readconfig.get_app_url())
        self.log.info("Navigated to URL:" + Readconfig.get_app_url())
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()
        self.log.info("*****test_login_ddt Started*****")

        self.login_page = LoginPage(self.driver)
        self.login_page.click_login_header()
        self.rows = get_row_count(self.path, "Sheet1")
        for r in range(2, self.rows + 1):
            username = read_data(self.path, "Sheet1", r, 1)
            password = read_data(self.path, "Sheet1", r, 2)
            exp_status = read_data(self.path, "Sheet1", r, 3)
            self.login_page.enter_login_credentials(username, password)
            self.login_page.click_submit_login()
            actual_title = self.driver.title
            if actual_title == "My Account" and exp_status == "Pass":
                assert True
                self.log.info("Login Successful")
                self.log.info("test_login_ddt Passed")
                self.login_page.click_my_account()
                self.login_page.click_logout()
                self.login_page.click_continue_homepage()
                self.login_page.click_login_header()
            elif actual_title != "My Account" and exp_status == "Fail":
                assert True
                self.log.info("Login Unsuccessful")
                self.log.info("test_login_ddt Passed")
            else:
                self.log.info("test_login_ddt Passed")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage_title.png")
                assert False
            self.log.info("*****test_login_ddt Completed*****")
