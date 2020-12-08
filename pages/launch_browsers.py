from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class GetBrowser:
    @staticmethod
    def launch_firefox_browser():

        try:
            options = Options()
            options.headless = False

            firefox_driver = webdriver.Firefox\
                (options=options,
                 executable_path=r'C:\Users\usman.zahid\Desktop\geckodriver\geckodriver-v0.28.0-win64\geckodriver.exe')
            return firefox_driver

        except Exception as e:
            print('Firefox Driver/Browser Not Found \n', e)

    @staticmethod
    def launch_chrome_browser():
        try:
            chrome_driver = webdriver.Chrome()
            return chrome_driver

        except Exception as e:
            print('Chrome Driver/Browser Not Found \n', e)
