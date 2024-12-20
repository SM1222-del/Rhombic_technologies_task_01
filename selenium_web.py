# selenium_web.py
from selenium import webdriver


#class to construct a function
class Infos:
    def __init__(self):
#initiate the driver
      self.query = None
      self.driver = webdriver.Chrome()

    def get_Info(self,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org")
        search=self.driver.find_element_by_xpath('//*["@id=searchinput"]')
        search.click()
        search.send_keys(query)
        enter=self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldsets/button')
        enter.click()
