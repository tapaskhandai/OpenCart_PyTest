from selenium import webdriver
import pytest
from utilities.customLogger import LogGenerator
from utilities.readProperties import Readconfig

log = LogGenerator.log_gen()


@pytest.fixture()
def setup():
    if Readconfig.get_browser_driver() == "chrome":
        driver = webdriver.Chrome()
        log.info("Chrome Browser Launched")
    elif Readconfig.get_browser_driver() == "edge":
        driver = webdriver.Edge()
        log.info("Edge Browser Launched")
    else:
        driver = webdriver.Chrome()
        log.info("Chrome Browser Launched")
    driver.get(Readconfig.get_app_url())
    log.info("Navigated to URL:" + Readconfig.get_app_url())
    driver.implicitly_wait(4)
    driver.maximize_window()
    return driver


##########PyTest Html Report##########

# Hook for adding env info to Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Open cart'
    config._metadata['Author'] = 'Tapas'


# Hook for delete/modify env info to Html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
