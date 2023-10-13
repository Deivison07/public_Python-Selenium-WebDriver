import json
from selenium.webdriver.chrome.options import Options

SELENIUM_DOWNLOAD_FOLDER_PATH = "C:\\Users\\note\\Documents\\download_folder_path"

class SeleniumOptionsBuilder:

    def __init__(self):
        self.prefs = {}
        self.options = Options()
        self.automation_controlled()
        self.options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
        )

        self.set_prefs("profile.default_content_settings.popups",0)
        self.set_prefs("download.default_directory",SELENIUM_DOWNLOAD_FOLDER_PATH)
        self.set_prefs("savefile.default_directory",SELENIUM_DOWNLOAD_FOLDER_PATH)
        self.set_prefs("download.prompt_for_download",False)
        self.set_prefs("safebrowsing.enabled", True)
        self.set_prefs("download.extensions_to_open", "xml")
        self.set_prefs("download.directory_upgrade", True)
        self.set_prefs("plugins.always_open_pdf_externally", True)

        self.prefs["printing.print_preview_sticky_settings.appState"] = json.dumps(
            {
                "recentDestinations": [
                    {
                        "id": "Save as PDF",
                        "origin": "local",
                        "account": "",
                    }
                ],
                "selectedDestinationId": "Save as PDF",
                "version": 2,
            }
        )
        
    def settings_default(self):

        self.start_maximized()
        self.ssl_erros()
        self.print_tela_cheia()
        self.desabilita_safe()
        return self

    def start_maximized(self):
        '''
         Inicia a janela do navegador maximizada, ou seja, em tela cheia.
        '''
        self.options.add_argument("start-maximized")
        self.options.add_argument("--window-size=1920,1080")
        return self

    def ssl_erros(self):
        '''
         Ignora erros relacionados a certificados SSL
         incluindo erros de validação e expiração
        '''
        self.options.add_argument("--ignore-ssl-errors=yes")
        self.options.add_argument("--ignore-certificate-errors")
        return self
    
    def print_tela_cheia(self):
        '''
         Esse modo permite que a impressão seja feita em tela cheia, ocultando outros elementos da página. 
        '''
        self.options.add_argument("--kiosk-printing")
        return self

    def desabilita_safe(self):
        '''
         Desativa a proteção de download do Google Safe Browsing
         Desativa a lista negra de extensões do Google Safe Browsing.
        '''
        self.options.add_argument("--safebrowsing-disable-download-protection")
        self.options.add_argument("safebrowsing-disable-extension-blacklist")
        return self

    def automation_controlled(self):
        '''
         ajudar a evitar a detecção automatizada do ChromeDriver
        '''
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        return self

    def set_prefs(self, arg:str, value):
        self.prefs[arg] = value
        return self

    def get_prefs(self):
        return self.prefs

    def remove_prefs(self,arg):
        try:
            del(self.prefs[arg])
        except KeyError:
            pass
    
    def add_argument(self, arg:str):
        self.options.add_argument(str(arg))
        return self

    def add_experimental(self, option:str, args:list|dict):
        self.options.add_experimental_option(str(option), args)
        return self
    
    def build(self) -> Options:
        self.options.add_experimental_option("prefs", self.prefs)
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        return self.options
