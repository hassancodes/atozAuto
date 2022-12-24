from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time
from secret import username,password
from mfa import fetch_mfa
from discordwebhook import Discord
from secret import urlhook 


chromedriver_autoinstaller.install()

login =None
mfa_auth=None
data = ""

# discord hook for alerting



shiftnotfound = '''<div data-test-component="StencilReactCol" class="css-1s0p9lu"><div data-test-component="StencilReactView" class="QuickLink_IconContainer css-fy50kh"><svg display="block" xmlns="http://www.w3.org/2000/svg" class="stencilSvgIcon css-14wvfj0" width="32" height="32" aria-hidden="true" focusable="false" viewBox="0 0 26 27" data-test-component="StencilFindShiftsIcon" style="width: 32px; height: 32px;"><path fill-rule="evenodd" fill="currentColor" d="M24.708 12.207h-.007v1.24l-2.571 1.376.003-.002v-4.727l2.575 1.618v.495Zm0 13.078H1.578V14.92l11.566 6.194 11.564-6.194v10.365ZM1.578 11.712l2.577-1.618v4.727l.001.002-2.57-1.376v-1.24h-.008v-.495Zm3.86-9.961h15.41v13.76l-7.704 4.127-7.705-4.128V1.751Zm20.54 10.456v-1.216l-3.845-2.415V.444H4.155v8.133L.309 10.991v1.216H.302v2.028l.007.004v12.338h25.668V14.239l.008-.004v-2.028h-.008Z"></path><path fill-rule="evenodd" fill="currentColor" d="M13.829 15.415a.201.201 0 0 0 .061-.15v-1.15c.73-.113 1.323-.412 1.779-.895a2.43 2.43 0 0 0 .685-1.73v.002c0-.22-.03-.425-.09-.618a2.353 2.353 0 0 0-.218-.502 1.703 1.703 0 0 0-.364-.416 4.227 4.227 0 0 0-.427-.328 4.109 4.109 0 0 0-.519-.28 9.896 9.896 0 0 0-1.08-.436c-.215-.08-.377-.14-.482-.181a9.78 9.78 0 0 1-.415-.177 2.418 2.418 0 0 1-.386-.204 3.173 3.173 0 0 1-.271-.217.748.748 0 0 1-.204-.271.836.836 0 0 1-.059-.316c0-.297.139-.54.413-.728.276-.189.632-.283 1.067-.283.193 0 .39.025.588.076a3.207 3.207 0 0 1 .915.38c.127.077.216.135.269.174.052.04.085.066.1.08.059.042.12.058.186.044a.188.188 0 0 0 .157-.104l.558-.958c.055-.089.044-.172-.034-.25a1.903 1.903 0 0 0-.104-.092 3.758 3.758 0 0 0-.268-.191 3.283 3.283 0 0 0-.437-.246 4.646 4.646 0 0 0-.599-.22 4.008 4.008 0 0 0-.76-.15V3.921a.199.199 0 0 0-.061-.15.222.222 0 0 0-.16-.06h-.929c-.06 0-.11.02-.154.062a.195.195 0 0 0-.066.148v1.181c-.72.132-1.305.425-1.754.88-.45.455-.675.984-.675 1.588 0 .18.02.35.059.512.039.162.086.308.144.437.058.13.139.256.244.381.106.124.206.232.3.32.094.091.217.184.368.28.15.097.28.174.389.234a9.465 9.465 0 0 0 .853.377l.422.164c.25.092.432.163.552.213.119.05.27.12.453.21.185.09.318.172.403.246.085.075.162.167.23.276a.64.64 0 0 1 .104.347c0 .346-.14.613-.423.802-.283.188-.61.282-.98.282-.17 0-.34-.017-.51-.053-.596-.113-1.154-.387-1.672-.82l-.013-.013a.175.175 0 0 0-.166-.06c-.073.01-.126.035-.158.08l-.709.886c-.069.087-.064.176.014.268.023.026.063.066.121.118.058.053.164.136.32.247.156.111.325.217.509.315.183.098.416.196.698.293.282.095.575.164.877.203v1.149a.2.2 0 0 0 .066.148.218.218 0 0 0 .155.062h.929a.22.22 0 0 0 .159-.06"></path></svg><div class="css-1aayaoq e1aayydo0">Find shifts</div></div><div data-test-component="StencilText" class="css-kyen4s">Find shifts</div></div>'''
def create_driver():
    Options = webdriver.ChromeOptions()
    Options.add_argument("start-maximized")
    Options.add_argument("disable-infobars")
    Options.add_experimental_option("useAutomationExtension", False)
    Options.add_experimental_option("excludeSwitches",["enable-automation"])
    driver= webdriver.Chrome(options=Options)
    return driver

driver = create_driver()

# def check_shift_available():
#     # first we need to get the element stored their
#     raw_quicklinks  = driver.find_elements(By.CLASS_NAME,value="css-1iicd35")
#     print(type(raw_quicklinks))
#     find_shifts_button = raw_quicklinks[0]


def send_message(alert):
    discord = Discord(url=urlhook)
    discord.post(content=alert)
    
    
    

# send_message("Hello")

def login():
    try: 
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
        mfa = fetch_mfa()
        print(mfa)
        driver.implicitly_wait(5)
        driver.find_element(By.ID,value="code").send_keys(mfa)
        driver.find_element(By.ID,value="trusted-device-option-label").click()
        driver.find_element(By.ID,value="buttonVerifyIdentity").click()
    except:
        send_message("error occured while logging in")




def check_drop_shift():
    driver.implicitly_wait(3)
    driver.get("https://atoz.amazon.work/shifts")
    driver.implicitly_wait(3)
    # driver.find_element(By.XPATH,value="//*[@id='atoz-shift-management-page-root']/div[1]/div[1]/div/div/div[1]/div/button[1]/div").click()
    #######***************-- we may need to change this class in the future as it is dynamic--***************########
    elem = driver.find_elements(By.CLASS_NAME,value="css-1s0p9lu")[0]
    element_source = elem.get_attribute("outerHTML")
    print(element_source)
    
    
    if(shiftnotfound==element_source):
        print(False)
        send_message("No available shift currently")
    elif(shiftnotfound != element_source):
    #invoke the function
        send_message("There is a shift available")
        print(True) 

        
        
def main():
    try: 
        login()
        while True:
            check_drop_shift()
            driver.implicitly_wait(10)
    except:
        # print("ending.....")
        # return
        # calling main function again
        driver.implicitly_wait(100)
        main()



if __name__ == "__main__":
    main()    