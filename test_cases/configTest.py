from selenium import webdriver
import pytest

from utilities.customLogger import LogGenerator
from utilities.readProperties import Readconfig


@pytest.fixture()
def setup():
    log = LogGenerator.log_gen()
    if Readconfig.get_browser_driver() == "chrome":
        driver = webdriver.Chrome()
        log.info("Chrome Browser Launched")
    elif Readconfig.get_browser_driver() == "edge":
        driver = webdriver.Edge()
        log.info("Edge Browser Launched")
    else:
        driver = webdriver.Chrome()
        log.info("Chrome Browser Launched")
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
