from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time
from mfa import main
chromedriver_autoinstaller.install()

def create_driver():
    Options = webdriver.ChromeOptions()
    Options.add_argument("start-maximized")
    Options.add_argument("disable-infobars")
    Options.add_experimental_option("useAutomationExtension", False)
    Options.add_experimental_option("excludeSwitches",["enable-automation"])
    driver= webdriver.Chrome(options=Options)
    return driver



def login():
     
    driver = create_driver()
    driver.get("https://google.com/")
    driver.get("https://atoz.amazon.work/")
    id="nhamuham"
    ps="atozevjr3303@A"
    driver.find_element(By.ID, value="login").send_keys(id)
    driver.find_element(By.ID, value="password").send_keys(ps)
    driver.find_element(By.ID,value="buttonLogin").click()
    time.sleep(3)
    driver.find_elements(By.CLASS_NAME, value="radio")[1].click()
    driver.find_element(By.ID,value="buttonContinue").click()
    

