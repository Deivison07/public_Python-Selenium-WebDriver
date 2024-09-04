from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

class Driver(webdriver.Chrome):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def _wait_element(self, by, value, condition=EC.presence_of_element_located, timeout=5):

        try:
            element = WebDriverWait(self, timeout).until(condition((by, value)))
        except TimeoutException:
            raise TimeoutException

        return element


    def _wait_element_click(
        self,
        by,
        value,
        timeout=5,
        fail_silently=False,
    ):
        element = self._wait_element(by, value, EC.element_to_be_clickable, timeout)

        if element:
            element.click()

    
        
            