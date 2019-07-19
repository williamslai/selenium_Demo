#coding=utf-8
from selenium import webdriver
driver = webdriver.Chrome()
#访问百度首页
first_url= 'http://www.baidu.com'
print ('變成全螢幕吧！！！！') 
driver.maximize_window()
print ("now access %s" %(first_url) )
driver.get(first_url)
#访问新闻页面 
second_url='http://news.baidu.com' 
print ("now access %s" %(second_url)) 
# driver.get(second_url)
# driver.get(first_url)
# driver.get(second_url)
# driver.get(first_url)
# third_url='https://www.google.com'
# print ("now access %s" %(third_url) )
# driver.get(third_url)

#返回(后退)到百度首页 
print ("back to %s"%(second_url))
driver.back()
#前进到新闻页
print ("forward to %s"%(second_url) )
driver.forward()
driver.quit()