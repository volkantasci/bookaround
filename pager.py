from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from bs4 import BeautifulSoup


class Pager:
    def __init__(self, page):
        self.item_count_div_spec = page.url.dist_site.item_count_div_spec
        self.page = page
        self.item_count = self.__item_count__
        self.driver = webdriver.Remote(self.page.command_executor, desired_capabilities=DesiredCapabilities.CHROME)
        self.sources = [self.page.page_source,]
        self.sources.extend(self.__page_sources__)

    @property
    def __item_count__(self) -> int:
        divs = self.item_count_div_spec.split('.')

        finding = BeautifulSoup(self.page.page_source)

        for div in divs:
            finding = finding.find('div', div)

        return int(finding.text.split()[0])

    @property
    def how_many_pages(self) -> int:
        if self.item_count % self.page.url.dist_site.page_size == 0:
            return self.item_count / self.page.url.dist_site.page_size

        else:
            return self.item_count // self.page.url.dist_site.page_size + 1

    @property
    def __page_sources__(self) -> list:
        sources = []
        for page_number in range(self.how_many_pages, 1, -1):
            self.driver.get(self.page.url.query_url + f'&{self.page.url.dist_site.pager_param}={page_number}')
            self.driver.implicitly_wait(3)
            sources.append(self.driver.page_source)

        self.driver.close()

        return sources
