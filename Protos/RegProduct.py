from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

productUrl = 'https://restaurante-dev.firebaseapp.com/#/product'
productName = 'Product1'       
productDescription = 'Description1'
productPrice = '10'
productImagePath = "D:/GitHub/SeleniumTest/AutoTest/Data/image.JPG"
import os
print(os.getcwd())
driver = webdriver.Chrome("./Driver/chromedriver.exe") 

#open browser
driver.get(productUrl)
driver.maximize_window()

#Type Name, description, price....
driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/div/div/div/div/form/div/div[2]/div[1]/div/div/input').send_keys(productName) 
driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/div/div/div/div/form/div/div[2]/div[2]/div/div/input').send_keys(productDescription) 
driver.find_element_by_xpath('//*[@id="Price"]').send_keys(productPrice) 
driver.find_element_by_xpath('//*[@id="mat-slide-toggle-1"]/label/div').click()

driver.find_element_by_xpath('//*[@id="mat-select-0"]/div/div[1]').click()
driver.find_element_by_xpath('//*[@id="mat-option-1"]/span').click()

#driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/div/div/div/div/form/div/div[2]/div[7]/div/div/div').click()
element = driver.find_element_by_id("file-input")
element.send_keys(productImagePath)

driver.close
#keep the browser open 
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)