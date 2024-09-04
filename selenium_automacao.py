import time
from selenium.webdriver.common.by import By
from driver.driver import Driver
from selenium.webdriver.chrome.options import Options

def site_selenium(browser: Driver):

    browser.get('https://pypi.org/project/selenium/')
    browser._wait_element_click(By.XPATH,  value='//*[@id="user-indicator"]/nav[1]/ul/li[2]/a')
    browser._wait_element_click(By.XPATH,  value='//*[@id="content"]/section/div/div[2]/div[4]/a')
    time.sleep(5)

