
from driver.driver import Driver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from SeleniumOptionsBuilder import SeleniumOptionsBuilder
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium_automacao import site_selenium

class App():

    def execute(self):
        
        customOptions = SeleniumOptionsBuilder().build()
        browser = Driver(
            service = webdriver.ChromeService(ChromeDriverManager().install()),
            options = customOptions)
        browser.delete_all_cookies()

        site_selenium(browser)
        
        browser.quit()     
        
if __name__ == '__main__':
    app = App()
    app.execute()

        
