from selenium import webdriver
from time import sleep

#引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome() 
driver.get("https://drive.google.com/drive/folders/15xFrdgBOtI3THxlTP38NWGfwGFi7N8QJ")
driver.maximize_window()
driver.find_element_by_id("identifierId").send_keys("****")
driver.find_element_by_id("identifierNext").click()
#driver.find_element_by_xpath("//*[@id="password"]/div[1]/div/span/div/span/span/span[2]").click()
sleep(2)#先用sleep，後續再改用wait
driver.find_element_by_css_selector(".whsOnd.zHQkBf").send_keys("****") 
driver.find_element_by_id("passwordNext").click()
sleep(5)#先用sleep，後續再改用wait
#定位到要右击的元素
right_click =driver.find_element_by_css_selector(".uXB7xe") #对定位到的元素执行鼠标右键操作 
ActionChains(driver).context_click(right_click).perform()
