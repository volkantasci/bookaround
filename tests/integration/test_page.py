from page import Page
from url import Url
from dist_site import DistSite
from unittest import TestCase


class PageTest(TestCase):
    def setUp(self) -> None:
        self.kidega_site = DistSite('Kidega', 'query', 'https://kidega.com/arama', 'searcHeadArea.txt', 20, 'page')
        self.idefix_site = DistSite('Idefix', 'Q', 'https://idefix.com/search', 'searcHeadArea.txt', 36, 'Page')
        self.url_kidega = Url(self.kidega_site, 'python')
        self.url_idefix = Url(self.idefix_site, 'python')

    def test_kidega_page(self):
        page = Page(self.url_kidega)
        self.assertIn('Volkan Taşçı', page.page_source)
        self.assertIn('Python Eğitim Kitabı', page.page_source)

    def test_idefix_page(self):
        page = Page(self.url_idefix)
        self.assertIn('Volkan Taşçı', page.page_source)
        self.assertIn('Python Eğitim Kitabı', page.page_source)
