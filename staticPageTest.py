# -*- coding: utf-8 -*-
from selenium import webdriver
import sys

def scroll_down(driver, increment):
   scheight = 0
   while scheight < 1:
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight*%s);" % scheight)
      scheight += increment

driver = webdriver.Chrome("/Users/christopherLee/Downloads/chromedriver")
#driver.implicitly_wait(300)
links = open(sys.argv[1], 'r')
for link in links:
   driver.get(link)
   # after page loads send javascript to slowly scroll down pagea
   page_height = driver.execute_script("return document.body.scrollHeight")
   #scheight = 0
   # three classes of pages, short, medium, long
   if page_height < 2000:
      #while scheight < 1:
      #   driver.execute_script("window.scrollTo(0, document.body.scrollHeight*%s);" % scheight)
      #   scheight += .001
      scroll_down(driver, .001)
   #elif page_height < 10000:
   #   scroll_down(driver, .0005)
   else:
      scroll_down(driver, .0001)

driver.quit()  
