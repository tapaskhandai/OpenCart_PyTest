from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


class SeleniumUtilities:

    @staticmethod
    def get_title(driver):
        try:
            return driver.title
        except Exception as e:
            print(f"Error while retrieving title: {e}")
            raise

    @staticmethod
    def mouse_hover_on_element(driver, element):
        try:
            action = ActionChains(driver)
            action.move_to_element(element).perform()
        except Exception as e:
            print(f"Error while hovering over element: {e}")
            raise

    @staticmethod
    def enter_text(element, text):
        try:
            element.clear()
            element.send_keys(text)
        except Exception as e:
            print(f"Error while sending text: {e}")
            raise

    @staticmethod
    def element_is_displayed(element):
        try:
            status = element.is_displayed()
            return status
        except Exception as e:
            print(f"Error while displaying element: {e}")
            raise

    @staticmethod
    def element_is_displayed_by_length(element):
        try:
            if len(element) > 1:
                return True
        except Exception as e:
            print(f"Error while displaying element: {e}")
            raise

    @staticmethod
    def get_text(element):
        try:
            text = element.text
            return text
        except Exception as e:
            print(f"Error while retrieving text: {e}")
            raise

    @staticmethod
    def get_first_selected_option_from_dropdown(element):
        try:
            select = Select(element)
            option = select.first_selected_option
            return option
        except Exception as e:
            print(f"Error while getting first option: {e}")
            raise
