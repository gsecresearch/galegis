# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 20:33:15 2016

@author: Devin
"""
import time
from selenium import webdriver
"""I think webdriver needs to be downloaded"""

driver = webdriver.Chrome('C:/temp/chromedriver_win32')
driver.get('http://www.google.com/xhtml')
time.sleep(5)
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()
