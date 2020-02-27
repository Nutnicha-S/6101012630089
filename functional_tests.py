from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_index(self):
        #เจนต้องการคิดเลข
        #เธฮจึงหา website ที่สามารถคำวณเลขได้
        #เธอเจอเว็บที่ต้องการแล้วจึงกดเข้าไป

        self.browser.get('http://127.0.0.1:8000/home')
        '''Test Only Index'''
        #เธอเห็นคำว่า Calculator อยู่บนชื่อเว็บ
        self.assertIn('', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Calculator', header_text)

        #เธอเห็น textbox X
        inputX_box = self.browser.find_element_by_id("num1")
        self.assertEqual(
            inputX_box.get_attribute('type'),
            'text'
        )
        #เธอใส่เลข 9 ลงไป
        inputX_box.send_keys('9')

        #เธอเห็น textbox Y
        inputY_box = self.browser.find_element_by_id("num2")
        self.assertEqual(
            inputY_box.get_attribute('type'),
            'text'
        )
        #เธอใส่เลข 8 ลงไป
        inputY_box.send_keys('8')

        #เธอเห็นปุ่ม +
        plus_button = self.browser.find_element_by_id("plus")
        self.assertEqual(
            plus_button.get_attribute('type'),
            'submit'
        )

        #เธอจึงกดปุ๋ม +
        plus_button.click()

        time.sleep(5)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')