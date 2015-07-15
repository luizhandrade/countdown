from selenium import webdriver
import datetime
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

# At the top of the page there is a big heading
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual("Countdown to the day", header_text)

# she a smaller heading saying what the time means 
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertEqual("Time left for 15 september.", header_text)
        
# She notice a date in top of the page
        header_text = self.browser.find_element_by_id('date_arrival').text
        self.assertEqual("How many days left to 2015/09/15?", header_text)

# Above theres a number 61
        date_arrival = datetime.datetime(2015, 9, 15)
        date_start = datetime.datetime(2015, 7, 15)
        date_holder = date_arrival - date_start

        days_text = self.browser.find_element_by_id('days').text
        self.assertEqual('61', days_text)
# She sees how many days are missing 
        self.fail('Finished the test!')
if __name__ == '__main__':
    unittest.main(warnings='ignore')
