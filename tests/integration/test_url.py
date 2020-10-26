from url import Url
from dist_site import DistSite
from unittest import TestCase


class UrlTest(TestCase):
    def setUp(self) -> None:
        self.site1_no_adt_params = DistSite('Kidega', 'query', 'https://kidega.com/arama', 'searcHeadArea.txt',
                                            20, 'page')
        self.site2_no_adt_params = DistSite('Idefix', 'Q', 'https://idefix.com/search',
                                            'TotalDocumentCount', 36, 'Page')
        self.site3_with_adt_params = DistSite('Kidega', 'query', 'https://kidega.com/arama', 'searcHeadArea.txt',
                                              20, 'page', {'categories[]': '30053'})
        self.site4_with_adt_params = DistSite('Idefix', 'Q', 'https://idefix.com/search', 'searcHeadArea.txt',
                                              36, 'Page', {'ActiveCategoryId': '11693'},)

        self.url1 = Url(self.site1_no_adt_params, 'python')
        self.url2 = Url(self.site2_no_adt_params, 'python')
        self.url3 = Url(self.site3_with_adt_params, 'python')
        self.url4 = Url(self.site4_with_adt_params, 'python')

    def test_no_adt_urls(self):
        self.assertEqual(self.url1.query_url, 'https://kidega.com/arama?query=python')
        self.assertEqual(self.url2.query_url, 'https://idefix.com/search?Q=python')
        self.assertEqual(self.url3.query_url, 'https://kidega.com/arama?query=python&categories[]=30053')
        self.assertEqual(self.url4.query_url, 'https://idefix.com/search?Q=python&ActiveCategoryId=11693')
