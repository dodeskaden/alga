import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
 
driver = webdriver.Firefox()
browser = webdriver.Firefox()
browser.get("https://algacard.ru/balance.php")
cardnumber= browser.find_element_by_id('cardnumber')
cardnumber.send_keys ('9643 10020 33005 04039')
cardnumber.submit()
time.sleep(10)
browser.save_screenshot('screen_test_alga.png')
