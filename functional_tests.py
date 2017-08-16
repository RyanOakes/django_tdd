import unittest
from selenium import webdriver


class NewVisiterTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Let's check out the to-do-list site
        self.browser.get('http://localhost:8000')

        # Ensure page title is accurate and I'm at the right website
        self.assertIn('To-Do Lists', self.browser.title)
        # self.fail('Finish the rest of the test')

        # TODO: Ability to add to-do item

if __name__ == '__main__':
    unittest.main()
