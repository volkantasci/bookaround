from url import Url
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class Page:
    def __init__(self, url: Url, command_executor="http://localhost:4444/wd/hub"):
        self.command_executor = command_executor
        self.query_url = url.query_url
        self.page_source = self.__get_page_source__()

    def __get_page_source__(self):
        driver = webdriver.Remote(command_executor=self.command_executor,
                                  desired_capabilities=DesiredCapabilities.CHROME)

        driver.get(self.query_url)
        driver.implicitly_wait(5)
        html = driver.page_source
        driver.close()

        return html
