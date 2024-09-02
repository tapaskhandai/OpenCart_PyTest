from selenium.webdriver.common.by import By


class LoginPageControls:
    link_my_account = "//span[normalize-space()='My Account']"
    link_login_my_account = "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Login']"
    textbox_email_login = "//input[@id='input-email']"
    textbox_password_login = "//input[@id='input-password']"
    button_submit_login = "//input[@value='Login']"

    def __init__(self, driver):
        self.driver = driver  # self.driver is class variable here

    def get_link_my_account(self):
        return self.driver.find_element(By.XPATH, self.link_my_account)

    def get_link_login_my_account(self):
        return self.driver.find_element(By.XPATH, self.link_login_my_account)

    def get_textbox_email_login(self):
        return self.driver.find_element(By.XPATH, self.textbox_email_login)

    def get_textbox_password_login(self):
        return self.driver.find_element(By.XPATH, self.textbox_password_login)

    def get_button_submit_login(self):
        return self.driver.find_element(By.XPATH, self.button_submit_login)
