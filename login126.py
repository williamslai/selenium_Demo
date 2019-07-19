#coding=utf-8
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.126.com")
driver.find_element_by_id("idInput").clear() 
driver.find_element_by_id("idInput").send_keys("username") 
driver.find_element_by_id("pwdInput").clear() 
driver.find_element_by_id("pwdInput").send_keys("password") 
driver.find_element_by_id("loginBtn").click()
driver.quit()