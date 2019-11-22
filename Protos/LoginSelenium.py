from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

username = 'chang'
password = 'password'
url = 'https://restaurante-dev.firebaseapp.com/#/login' 
driver = webdriver.Chrome("./Driver/chromedriver.exe") 

#open browser
driver.get(url)
driver.maximize_window()

#type credentials 
driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/div/div/div/div/div/form/div[1]/input').send_keys(username)
driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/div/div/div/div/div/form/div[2]/input').send_keys(password)

#click login button 
driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/div/div/div/div/div/form/div[3]/div/button').click()
driver.close
#keep the browser open 
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)