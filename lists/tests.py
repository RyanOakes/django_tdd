from lists.views import home_page
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        '''
        resolve is the function Django uses internally to resolve URLs and find
        what view function they should map to.  We are checking that resolve, when
        called with “/”, the root of the site, finds a function called home_page.
        '''
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do Lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
