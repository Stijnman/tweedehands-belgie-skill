import unittest
from urllib.parse import unquote_plus, urlsplit
from scripts.build_search_url import build_2dehands

class SearchURLTests(unittest.TestCase):
    def test_spaces_and_unicode(self):
        url = build_2dehands("  plafond lamp café  ")
        self.assertEqual(unquote_plus(urlsplit(url).path[3:-1]), "plafond lamp café")
    def test_query_cannot_change_host_or_fragment(self):
        url = urlsplit(build_2dehands("x/../../?q=1#fragment"))
        self.assertEqual(url.netloc, "www.2dehands.be")
        self.assertEqual(url.query, "")
        self.assertEqual(url.fragment, "")
        self.assertEqual(url.path.count("/"), 3)
