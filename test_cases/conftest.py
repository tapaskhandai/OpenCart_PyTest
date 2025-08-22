import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from utilities.customLogger import LogGenerator
from utilities.readProperties import Readconfig

log = LogGenerator.log_gen()


@pytest.fixture(autouse=True)
def setup(request):
    browser = Readconfig.get_browser()

    if browser == "chrome":
        chrome_opt = ChromeOptions()
        chrome_opt.add_experimental_option("excludeSwitches", ["enable-automation"])
        if Readconfig.get_headless() == "true":
            chrome_opt.add_argument("--headless=new")
        if Readconfig.get_incognito() == "true":
            chrome_opt.add_argument("--incognito")
        driver = webdriver.Chrome(options=chrome_opt)
        log.info("Chrome Browser Launched")

    elif browser == "edge":
        edge_opt = EdgeOptions()
        if Readconfig.get_headless() == "true":
            edge_opt.add_argument("--headless=new")
        if Readconfig.get_incognito() == "true":
            edge_opt.add_argument("--inprivate")
        driver = webdriver.Edge(options=edge_opt)
        log.info("Edge Browser Launched")

    else:
        driver = webdriver.Chrome()
        log.info("Default: Chrome Browser Launched")

    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(Readconfig.get_app_url())
    log.info("Navigated to URL: " + Readconfig.get_app_url())

    # Attach driver to test class
    request.cls.driver = driver

    yield

    driver.quit()
    log.info("Browser closed")


# Hook for Allure screenshot on failure
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        log.info("failed here")
        driver = getattr(item.cls, "driver", None)
        screenshot = driver.get_screenshot_as_png()
        log.info("taken screenshot")
        allure.attach(
            screenshot,
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        log.info("attached screenshot")
