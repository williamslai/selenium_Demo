#coding=utf-8
from selenium import webdriver
driver = webdriver.Chrome() 
driver.get("https://www.gamer.com.tw/")
driver.find_element_by_id('gsc-i-id1').send_keys('人中之龍') #提交输入框的内容
driver.find_element_by_id('gsc-i-id1').submit()
driver.quit()
