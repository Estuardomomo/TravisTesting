import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import uuid 
import os
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class FullTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls): 
        cls.driver = webdriver.Chrome("./Driver/chromedriver.exe") 
        cls.username = 'chang'
        cls.password = 'password'
        cls.driver.maximize_window()
        cls.tempID = str(uuid.uuid1())
        cls.driver.session_id
 
    def test_Login(self):
        driver = self.driver
        loginUrl = 'https://restaurante-dev.firebaseapp.com/#/login' 
        dashboardurl = 'https://restaurante-dev.firebaseapp.com/#/dashboard'
        #open browser
        driver.get(loginUrl)
        self.assertIn(loginUrl, driver.current_url)
        navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
        responseStart = driver.execute_script("return window.performance.timing.responseStart")
        domComplete = driver.execute_script("return window.performance.timing.domComplete")

        #type credentials 
        driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/div/div/div/div/div/form/div[1]/input').send_keys(self.username)
        driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/div/div/div/div/div/form/div[2]/input').send_keys(self.password)

        #click login button 
        driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/div/div/div/div/div/form/div[3]/div/button').click()
        print("Login successfull")

        #Calculate the performance
        backendPerformance_calc = responseStart - navigationStart
        frontendPerformance_calc = domComplete - responseStart
        print("Back End: %s ms" % backendPerformance_calc)
        print("Front End: %s ms" % frontendPerformance_calc)
        
    def test_Register(self):
        registerUrl = "https://restaurante-dev.firebaseapp.com/#/register"
        nombre = 'name ' + self.tempID
        apellido = 'surname ' + self.tempID
        correo = 'correo' + self.tempID + '@gmail.com'
        user = 'user ' + self.tempID
        driver = self.driver
        timeout = 3

        #open browser      
        driver.get(registerUrl) 
        try:
            element_present = EC.presence_of_element_located((By.ID, 'main'))
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
        try:
            self.assertIn(registerUrl, driver.current_url)
        except:
            time.sleep(2)   
            driver.get(registerUrl)
        navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
        responseStart = driver.execute_script("return window.performance.timing.responseStart")
        domComplete = driver.execute_script("return window.performance.timing.domComplete")

        #type credentials
        
        driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/app-dashboard/div/div/main/div/div/div/div/div/form/div[2]/input[1]').send_keys(nombre)
        driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/app-dashboard/div/div/main/div/div/div/div/div/form/div[2]/input[2]').send_keys(apellido)
        driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/app-dashboard/div/div/main/div/div/div/div/div/form/div[3]/input').send_keys(correo)
        driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/app-dashboard/div/div/main/div/div/div/div/div/form/div[4]/input').send_keys(user)
        driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/app-dashboard/div/div/main/div/div/div/div/div/form/div[5]/input').send_keys(self.password)
        driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/app-dashboard/div/div/main/div/div/div/div/div/form/div[6]/input').send_keys(self.password) 

        #click create account 
        #driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/app-dashboard/div/div/main/div/div/div/div/div/form/div[7]/button').click()

        print("Register User successfull")
        #Calculate the performance
        backendPerformance_calc = responseStart - navigationStart
        frontendPerformance_calc = domComplete - responseStart
        print("Back End: %s ms" % backendPerformance_calc)
        print("Front End: %s ms" % frontendPerformance_calc)

    def test_Register_Product(self):
        productUrl = 'https://restaurante-dev.firebaseapp.com/#/product'
        #tempID = uuid.uuid1()
        productName = 'Product' + self.tempID      
        productDescription = 'Description1' + self.tempID
        productPrice = '10'
        workingDirectory = os.getcwd()
        productImagePath = workingDirectory.replace("\\","/") + "/Data/image.JPG"
        driver = self.driver
        timeout = 3
        #open browser   
        

        #open browser      
        driver.get(productUrl) 
        try:
            element_present = EC.presence_of_element_located((By.ID, 'main'))
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
        try:
            self.assertIn(productUrl, driver.current_url)
        except:
            time.sleep(2)   
            driver.get(productUrl)
        navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
        responseStart = driver.execute_script("return window.performance.timing.responseStart")
        domComplete = driver.execute_script("return window.performance.timing.domComplete")

        #Type Name, description, price....
        driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/app-dashboard/div/div/main/div/div/div/div/div/form/div/div[2]/div[1]/div/div/input').send_keys(productName) 
        driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/app-dashboard/div/div/main/div/div/div/div/div/form/div/div[2]/div[2]/div/div/input').send_keys(productDescription) 
        driver.find_element_by_xpath('//*[@id="Price"]').send_keys(productPrice) 
        #Disponible
        driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/app-dashboard/div/div/main/div/div/div/div/div/form/div/div[2]/div[6]/div[1]/div/div/mat-slide-toggle/label/div').click()
        
        #select category
        driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/app-dashboard/div/div/main/div/div/div/div/div/form/div/div[2]/div[6]/div[2]/div[1]/mat-select/div/div[1]').click()
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/mat-option[2]/mat-pseudo-checkbox').click() #.send_keys(Keys.ESCAPE)
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/mat-option[3]/mat-pseudo-checkbox').click()
        driver.find_element_by_xpath('/html/body/div[2]/div[1]').click()
        
        #upload image
        element = driver.find_element_by_id("file-input")
        element.send_keys(productImagePath)

        #click crear producto
        #driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/app-dashboard/div/div/main/div/div/div/div/div/form/div/div[3]/button').click()
        print("Register New Product successfull")

        #Calculate the performance
        backendPerformance_calc = responseStart - navigationStart
        frontendPerformance_calc = domComplete - responseStart
        print("Back End: %s ms" % backendPerformance_calc)
        print("Front End: %s ms" % frontendPerformance_calc)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

if __name__ == "__main__":
    unittest.main()