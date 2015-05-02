import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):

	def setUP(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
	
	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):

		browser.get('http://localhost:8000')

assert 'Django' in browser.title
