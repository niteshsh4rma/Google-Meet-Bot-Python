from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1, 
    "profile.default_content_setting_values.geolocation": 0, 
    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome("../chromedriver.exe", options=opt)

def login(mail_address, password):
    driver.get('https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ') 

    driver.find_element_by_id("identifierId").send_keys(mail_address) 
    driver.find_element_by_id("identifierNext").click() 
    driver.implicitly_wait(10) 
  
    driver.find_element_by_xpath( 
        '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password) 
    driver.implicitly_wait(10) 
    driver.find_element_by_id("passwordNext").click() 
    driver.implicitly_wait(10) 
  
    driver.get('https://google.com/') 
    driver.implicitly_wait(100) 


def JoinNow(link, email_address, password, time_diff):
    login(email_address, password)
    driver.implicitly_wait(5000)
    driver.get(link)

    time.sleep(5)
    driver.find_element_by_xpath( 
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div/div/div').click() 
    driver.implicitly_wait(3000) 
  
    time.sleep(1) 
    driver.find_element_by_xpath( 
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div').click() 
    driver.implicitly_wait(3000)  

    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]').click()

    time.sleep(time_diff*60)

    driver.close()



