#youtube automation
from selenium import webdriver

class music():
    def __init__(self):
        self.query = None
        self.driver= webdriver.chrome

    def play(self,query):
        self.query=query
        self.driver.get(url="https://www.youtube.com/results?search_query=".query)
        video=self.driver_find_element_by_xpath('//*[@id="dismissible"]')
        video.click()