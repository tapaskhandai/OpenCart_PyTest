from selenium.webdriver.common.by import By


class MyAccountPageControls:
    button_logout_homepage = "//a[normalize-space()='Logout']"
    button_continue_homepage = "//a[@class='btn btn-primary']"
    success_msg_account_updated = "//div[contains(text(),'Success: Your account')]"
    link_edit_account_info = "//a[normalize-space()='Edit your account information']"
    textbox_firstname_edit_info = "//input[@id='input-firstname']"
    textbox_lastname_edit_info = "//input[@id='input-lastname']"
    textbox_telnum_edit_info = "//input[@id='input-telephone']"
    button_continue_edit_info = "//input[@value='Continue']"
    link_change_password = "//a[normalize-space()='Change your password']"
    textbox_password_change_password = "//input[@id='input-password']"
    textbox_confirm_password_change_password = "//input[@id='input-confirm']"
    error_msg_change_password = "//div[contains(text(),'Password confirmation does not match password!')]"
    link_components = "//a[normalize-space()='Components']"

    def __init__(self, driver):
        self.driver = driver  # self.driver is class variable here

    def get_link_edit_account_info(self):
        return self.driver.find_element(By.XPATH, self.link_edit_account_info)

    def get_textbox_firstname_edit_info(self):
        return self.driver.find_element(By.XPATH, self.textbox_firstname_edit_info)

    def get_textbox_lastname_edit_info(self):
        return self.driver.find_element(By.XPATH, self.textbox_lastname_edit_info)

    def get_textbox_telnum_edit_info(self):
        return self.driver.find_element(By.XPATH, self.textbox_telnum_edit_info)

    def get_button_continue_edit_info(self):
        return self.driver.find_element(By.XPATH, self.button_continue_edit_info)

    def get_success_msg_account_updated(self):
        return self.driver.find_element(By.XPATH, self.success_msg_account_updated)

    def get_link_change_password(self):
        return self.driver.find_element(By.XPATH, self.link_change_password)

    def get_textbox_password_change_password(self):
        return self.driver.find_element(By.XPATH, self.textbox_password_change_password)

    def get_textbox_confirm_password_change_password(self):
        return self.driver.find_element(By.XPATH, self.textbox_confirm_password_change_password)

    def get_error_msg_change_password(self):
        return self.driver.find_element(By.XPATH, self.error_msg_change_password)

    # def capture_success_msg_account_updated(self):
    #     return self.driver.find_element(By.XPATH, self.success_msg_account_updated).text

    def get_link_components(self):
        return self.driver.find_element(By.XPATH, self.link_components)

    def get_button_logout_homepage(self):
        return self.driver.find_element(By.XPATH, self.button_logout_homepage)

    def get_button_continue_homepage(self):
        return self.driver.find_element(By.XPATH, self.button_continue_homepage)
