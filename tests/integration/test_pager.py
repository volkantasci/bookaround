from pager import Pager
from page import Page
from url import Url
from dist_site import DistSite
from unittest import TestCase


class PagerTest(TestCase):
    def setUp(self) -> None:
        self.dist1 = DistSite('Kidega', 'query', 'https://kidega.com/arama', 'searcHeadArea.txt', 20, 'page')
        self.url1 = Url(self.dist1, 'python')
        self.page1 = Page(self.url1)
        self.pager1 = Pager(self.page1)

    def test_item_count(self):
        self.assertEqual(self.pager1.item_count, 32)

    def test_page_count(self):
        self.assertEqual(len(self.pager1.sources), 2)
