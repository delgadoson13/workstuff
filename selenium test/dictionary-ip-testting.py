from selenium import webdriver
import selenium, time
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

PATH = "C:\Program Files (x86)\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
app_server_ips = {'APP3':'10.1.1.125', 'APP4':'10.1.1.126', 'APP5':'10.1.1.122'}

for key, value in app_server_ips.items():
    url = f'http://{value}/eSchoolPLUS/Account/LogOn?ReturnUrl=%2feschoolplus'
    #print(url)
    driver.get(url)
    username = driver.find_element_by_id("UserName")
    username.send_keys("114695")
    username.send_keys(Keys.RETURN)
    pw = driver.find_element_by_id("Password")
    pw.send_keys("MTbel.1126.Sk8!")
    pw.send_keys(Keys.RETURN)
    driver.find_element_by_xpath("//div[@class='sg-result-container']").click()
    driver.find_element_by_xpath("//*[contains(text(), 'SAN_Live')]").click()
    time.sleep(3) #seconds -- This was needed because of the Javascript:Void(0) message
    #driver.find_element_by_xpath("//div[@class='select2-drop-mask']").click()
    #driver.find_element_by_xpath("//*[contains(text(), '2020-21 (Current Year)')]").click()
    driver.find_element_by_xpath("//button[@id='setEnvOkButton']").click()
    #okbutton.click()
    time.sleep(5)
    #driver.quit()
    #time.sleep(2)
    print(f'{key} testing was successfull.')
driver.quit()