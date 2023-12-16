from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class Ritesh:
    def __init__(self, url):
       self.url = url
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
       self.username = 'Admin'
       self.password = 'admin123'


    
    def login(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value='username').send_keys(self.username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(self.password)

        sleep(2)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

        sleep(3)
        self.driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]').click()                         
        sleep(3)

    
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[8]/div/div[9]/div/button[2]/i').click()


        self.firstName = '#guvi'
        self.middleName = '#zen'
        self.lastName = '#class'


        sleep(5)
        self.driver.find_element(by=By.NAME, value='firstName').send_keys(self.firstName)

        self.driver.find_element(by=By.NAME, value='middleName').send_keys(self.middleName)

        
        self.driver.find_element(by=By.NAME, value='lastName').send_keys(self.lastName)



        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button').click()



        


url = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPimModule'

Ritesh(url).login()