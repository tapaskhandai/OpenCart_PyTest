import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\tapas\\PycharmProjects\\OpenCart_PyTest\\configurations\\config.ini")


class Readconfig:

    @staticmethod
    def get_browser():
        browser_name = config.get('browser info', 'browser_name')
        return browser_name

    @staticmethod
    def get_headless():
        headless_option = config.get('browser info', 'headless')
        return headless_option

    @staticmethod
    def get_incognito():
        incognito_option = config.get('browser info', 'incognito')
        return incognito_option

    @staticmethod
    def get_app_url():
        url = config.get('common info', 'baseUrl')
        return url

    @staticmethod
    def get_username():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def get_excel_file_path():
        path = config.get('common info', 'excel_file_path')
        return path
