from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
import time
import sys

username = sys.argv[1]
password = sys.argv[2]


chromedriver = "./chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get("https://outlook.live.com/owa/?nlp=1")

driver.find_element_by_name("loginfmt").send_keys(username)
driver.implicitly_wait(10)
signIn = driver.find_element_by_id("idSIButton9")
driver.execute_script("arguments[0].click();", signIn)
driver.implicitly_wait(50)
driver.find_element_by_id("username").send_keys(username.split('@')[0])
driver.find_element_by_id("password").send_keys(password)
driver.implicitly_wait(5)
driver.find_element_by_name("submit").click()
driver.implicitly_wait(100)
# a = driver.find_element_by_xpath('//button[text()="Send Me a Push "]')
driver.find_element_by_name("DontShowAgain").click()
signIn = driver.find_element_by_id("idSIButton9")
driver.execute_script("arguments[0].click();", signIn)

driver.implicitly_wait(30)
emails = driver.find_elements_by_xpath("//div[@aria-label]")


for email in emails:
    try:

        if "Appointment" in email.get_attribute("aria-label"):
            if "CS2340: Objects and Design" in email.get_attribute("aria-label"):
                check = email.find_element_by_xpath(".//i[@data-icon-name='StatusCircleCheckmark']")
                driver.execute_script("arguments[0].click();", check)
    except StaleElementReferenceException as e:
        print(e)
        pass



driver.implicitly_wait(10)
delete = driver.find_element_by_name("Delete")
driver.execute_script("arguments[0].click();", delete)


# print(a)
# a.click()
