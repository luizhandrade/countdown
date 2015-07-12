from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_view_countdown_clock(self):
# Jacq goes to the countdown site
        self.browser.get('http://localhost:8001')

# She notice the title confirming this is the right site.
        self.assertIn('Countdown', self.browser.title)
        self.fail('Finished the test!')
        
# She sees this is a countdown to a specific date "september"

if __name__ == '__main__':
    unittest.main(warnings='ignore')
