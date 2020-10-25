from unittest import TestCase
from shortcuts import DistSite


class DistSiteTest(TestCase):
    def setUp(self) -> None:
        self.site1 = DistSite('Kidega', 'query', 'https://kidega.com/arama')

    def test_attributes(self):
        self.assertEqual('Kidega', self.site1.name)
        self.assertEqual('https://kidega.com/arama', self.site1.search_url)
        self.assertEqual('query', self.site1.search_param)
