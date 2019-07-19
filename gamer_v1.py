#coding=utf-8
from selenium import webdriver
driver = webdriver.Chrome() 
driver.get("https://www.gamer.com.tw/")
#获得输入框的尺寸 
size=driver.find_element_by_id('gsc-i-id1').size 
print (size)
#返回百度页面底部备案信息 
#text=driver.find_element_by_id("gnn_normal").text 
#print (text)
#返回元素的属性值，可以是 id、name、type 或元素拥有的其它任意属性 
attribute=driver.find_element_by_id("gnn_normal").get_attribute('type') 
print (attribute)
#返回元素的结果是否可见，返回结果为 True 或 False 
result=driver.find_element_by_id("gnn_normal").is_displayed() 
print (result)