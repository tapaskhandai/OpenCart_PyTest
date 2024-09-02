from selenium.webdriver import ActionChains
from selenium import webdriver


class SeleniumUtilities:

    @staticmethod
    def mouse_hover_on_element(self, driver, element):
        try:
            action = ActionChains(driver)
            action.move_to_element(element).perform()
        except Exception as e:
            print(f"Error while hovering over element: {e}")
            raise

    @staticmethod
    def enter_text(self, element, text):
        try:
            element.clear()
            element.send_keys(text)
        except Exception as e:
            print(f"Error while sending text: {e}")
            raise

    @staticmethod
    def element_is_displayed(self, element):
        try:
            status = element.is_displayed()
            return status
        except Exception as e:
            print(f"Error while displaying element: {e}")
            raise

    @staticmethod
    def get_text(self, element):
        try:
            text = element.text
            return text
        except Exception as e:
            print(f"Error while retrieving text: {e}")
            raise
