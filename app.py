from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time
from secret import username,password
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
    id=username
    ps=password
    driver.find_element(By.ID, value="login").send_keys(id)
    driver.find_element(By.ID, value="password").send_keys(ps)
    driver.find_element(By.ID,value="buttonLogin").click()
    time.sleep(3)
    driver.find_elements(By.CLASS_NAME, value="radio")[1].click()
    driver.find_element(By.ID,value="buttonContinue").click()
    mfa = main()
    print(mfa)
    driver.implicitly_wait(5)
    driver.find_element(By.ID,value="code").send_keys(mfa)
    driver.find_element(By.ID,value="trusted-device-option-label").click()
    driver.find_element(By.ID,value="buttonVerifyIdentity").click()
    while True:
        pass
login()
    
    

