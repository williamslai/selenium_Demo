#coding=utf-8
from selenium import webdriver
driver = webdriver.Firefox()
#访问百度首页
first_url= 'http://www.baidu.com' print "now access %s" %(first_url) driver.get(first_url)
#访问新闻页面 second_url='http://news.baidu.com' print "now access %s" %(second_url) driver.get(second_url)