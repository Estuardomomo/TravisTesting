from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.webdriver.common.keys import Keys

username = 'chang'
password = 'password'
url = 'https://restaurante-dev.firebaseapp.com/#/register'
driver = webdriver.Chrome("./Driver/chromedriver.exe")    #msedgedriver chromedriver   geckodriver
nombre = 'nombre'       
apellido = 'apellido'
correo = 'correo'

#open browser
driver.get(url)
driver.maximize_window()

#type credentials
driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/div/div/div/div/form/div[2]/input[1]').send_keys(nombre)
driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/div/div/div/div/form/div[2]/input[2]').send_keys(apellido)
driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/div/div/div/div/form/div[3]/input').send_keys(correo)
driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/div/div/div/div/form/div[4]/input').send_keys(username)
driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/div/div/div/div/form/div[5]/input').send_keys(password)
driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/div/div/div/div/form/div[6]/input').send_keys(password) 