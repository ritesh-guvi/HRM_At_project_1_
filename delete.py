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

    
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[4]/div/div[9]/div/button[1]/i').click()


        sleep(2)
        
        self.driver.find_element(by=By.XPATH, value='/html/body/div/div[3]/div/div/div/div[3]/button[2]').click()

url = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPimModule'

Ritesh(url).login()