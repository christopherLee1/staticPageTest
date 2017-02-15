#!/bin/env/python3 
'''
This small script takes a file of urls as input and simply
loads the web page and scrolls to the bottom, somewhat slow
enough for the eye to catch any errrors.
'''

from selenium import webdriver
import sys

def scroll_down(driver, increment):
   scheight = 0
   while scheight < 1:
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight*%s);" % scheight)
      scheight += increment

driver = webdriver.Chrome("/Users/christopherLee/Downloads/chromedriver")
links = open(sys.argv[1], 'r')
for link in links:
   if link[0:1] == ('#'):
      continue
   else:
      driver.get(link)
      # after page loads send javascript to slowly scroll down pagea
      page_height = driver.execute_script("return document.body.scrollHeight")
      if page_height < 2000: # smaller pages
         scroll_down(driver, .001)
      else: # larger pages need a slightly slower scroll
         scroll_down(driver, .0001)

driver.quit()  
