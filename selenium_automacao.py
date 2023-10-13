from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def site_selenium(browser):

    browser.get('https://pypi.org/project/selenium/')
    element = browser._wait_element(By.ID, 'description')