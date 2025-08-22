from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page_objects_controls.LoginPageControls import LoginPageControls
from page_objects_controls.MyAccountPageControls import MyAccountPageControls
from test_cases.conftest import *
from utilities.XLUtils import *
from utilities.customLogger import LogGenerator
from utilities.readProperties import Readconfig
from utilities.seleniumUtilities import SeleniumUtilities


@pytest.mark.usefixtures("setup")  # Automatically use the setup fixture
class TestLoginDDT:
    driver: WebDriver  # 👈 Tell the IDE this attribute exists
    log = LogGenerator.log_gen()

    @pytest.mark.regression
    def test_login_ddt(self):
        self.log.info("*****test_login_ddt Started*****")
        self.login_page = LoginPageControls(self.driver)
        self.login_page.get_link_my_account().click()
        self.login_page.get_link_login_my_account().click()
        self.rows = get_row_count(Readconfig.get_excel_file_path(), "Sheet1")
        for r in range(2, self.rows + 1):
            username = read_data(Readconfig.get_excel_file_path(), "Sheet1", r, 1)
            password = read_data(Readconfig.get_excel_file_path(), "Sheet1", r, 2)
            exp_status = read_data(Readconfig.get_excel_file_path(), "Sheet1", r, 3)
            SeleniumUtilities.enter_text(self.login_page.get_textbox_email_login(), username)
            SeleniumUtilities.enter_text(self.login_page.get_textbox_password_login(), password)
            self.login_page.get_button_submit_login().click()
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Qafox.com']")))
            actual_title = SeleniumUtilities.get_title(self.driver)
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
                self.log.info("test_login_ddt Failed")
                assert False
            self.log.info("*****test_login_ddt Completed*****")
